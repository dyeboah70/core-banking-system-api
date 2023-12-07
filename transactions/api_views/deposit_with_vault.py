from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json
from managers.decorators import check_permission
from transactions.decorators import is_teller
from accounts.models import Accounts
from transactions.models import Transactions
from deposits.models import DepositType, Deposits, TellerVault
from transactions.utils import generate_transaction_reference
from dateutil.relativedelta import relativedelta
from django.utils import timezone
from managers.tasks import (
    send_deposit_notification_sms,
    send_deposit_notification_email,
)

from django.db import transaction as db_transaction


@csrf_exempt
@require_POST
@check_permission("transaction")
@is_teller
@db_transaction.atomic
def deposit(request, teller=None):
    try:
        data = json.loads(request.body)
        amount = data.get("amount")
        account_number = data.get("account_number")
        narration = data.get("narration")
        deposit_type = data.get("deposit_type")

        if any(item == "" for item in [amount, account_number, deposit_type]) is None:
            return JsonResponse(
                {
                    "message": "Missing parameters in request",
                    "status": 400,
                },
                status=400,
            )

        # get the account
        try:
            with db_transaction.atomic():
                account = Accounts.objects.get(account_number=account_number)
                deposit_type = DepositType.objects.get(id=int(deposit_type))
                vault = TellerVault.objects.filter(teller=teller)
                vault_amount = vault.values("vault__amount")

                # if not account.user.is_approved:
                #     return JsonResponse(
                #         {
                #             "message": "Account is not verified",
                #             "status": 400,
                #         },
                #         status=400,
                #     )

                if not account.initial_deposit_date:
                    now = timezone.now()
                    next_interest_month = int(
                        12 / account.account_type.interest_calculation_per_year
                    )
                    account.initial_deposit_date = now
                    account.interest_start_date = now + relativedelta(
                        months=+next_interest_month
                    )
                transaction = Transactions.objects.create(
                    user=account.user,
                    amount=amount,
                    teller_id=teller.profile_id,
                    account_number=account_number,
                    transaction_type="deposit",
                )
                deposit = Deposits.objects.create(
                    user=account.user, narration=narration, deposit_type=deposit_type
                )
                deposit.amount += int(amount)
                deposit.save()
                account.balance += int(amount)
                account.save(
                    update_fields=[
                        "initial_deposit_date",
                        "balance",
                        "interest_start_date",
                    ]
                )

                name = f"{account.user.first_name} {account.user.last_name}"
                transaction.reference_number = generate_transaction_reference(name)
                transaction.save()

                if vault_amount is not None:
                    # Add deposit amount to the vault_amount
                    print(vault_amount[0]["vault__amount"])
                    print(int(amount))
                    vault_obj = vault.first()
                    vault_obj.vault.amount += int(amount)
                    vault_obj.vault.save()

        except Accounts.DoesNotExist:
            return JsonResponse(
                {
                    "message": "Account does not exist",
                    "status": 400,
                },
                status=400,
            )

        except DepositType.DoesNotExist:
            return JsonResponse(
                {
                    "message": "Deposit type does not exist",
                    "status": 400,
                },
                status=400,
            )

        send_deposit_notification_sms.delay(
            account.user.mobile_number, amount, account.balance
        )
        send_deposit_notification_email.delay(
            account.user.email, amount, account.balance
        )

        return JsonResponse(
            {
                "message": f"Transaction created successfully for {account_number} account for {amount} amount",
                "status": 200,
            }
        )

    except json.decoder.JSONDecodeError:
        return JsonResponse(
            {
                "message": "Invalid JSON",
                "status": 400,
            },
            status=400,
        )
