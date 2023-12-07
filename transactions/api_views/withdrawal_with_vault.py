from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json
from managers.decorators import check_permission
from transactions.decorators import is_teller
from accounts.models import Accounts
from transactions.models import Transactions
from withdrawals.models import Withdrawals
from transactions.utils import generate_transaction_reference
from deposits.models import TellerVault
from managers.tasks import (
    send_withdrawal_notification_sms,
    send_withdrawal_notification_email,
)
from django.http import JsonResponse

from django.db import transaction as db_transaction


@csrf_exempt
@require_POST
@check_permission("transaction")
@is_teller
@db_transaction.atomic
def withdrawal_with_vault(request, teller=None):
    try:
        data = json.loads(request.body)
        amount = data.get("amount")
        account_number = data.get("account_number")
        narration = data.get("narration")

        if any(item == "" for item in [amount, account_number]) is None:
            return JsonResponse(
                {
                    "message": "Missing parameters in request",
                    "status": 400,
                },
                status=400,
            )

        with db_transaction.atomic():  # Use the renamed module
            # get the account
            try:
                account = Accounts.objects.get(account_number=account_number)
                vault = TellerVault.objects.filter(teller=teller)
                vault_amount = vault.values("vault__amount")

                name = f"{account.user.first_name} {account.user.last_name}"
                transaction = Transactions.objects.create(
                    user=account.user,
                    amount=amount,
                    teller_id=teller.profile_id,
                    account_number=account_number,
                    transaction_type="withdrawal",
                )
                withdrawal = Withdrawals.objects.create(
                    user=account.user, narration=narration
                )
                withdrawal.amount += int(amount)
                withdrawal.save()
                account.balance -= int(amount)
                account.save()
                transaction.reference_number = generate_transaction_reference(name)
                transaction.save()

                if vault_amount is not None:
                    vault_obj = vault.first()
                    vault_obj.vault.amount -= int(amount)
                    vault_obj.vault.save()

                if account.balance < int(amount):
                    return JsonResponse(
                        {
                            "message": f"Account balance is {account.balance}, You cannot withdraw more than your account balance",
                            "status": 400,
                        },
                        status=400,
                    )

                max_withdraw_amount = account.account_type.maximum_withdrawal_amount
                if int(amount) > max_withdraw_amount:
                    return JsonResponse(
                        {
                            "message": f"Maximum withdrawal amount is {max_withdraw_amount} for {account.account_type.account_type}",
                            "status": 400,
                        },
                        status=400,
                    )

            except Accounts.DoesNotExist:
                return JsonResponse(
                    {
                        "message": "Account does not exist",
                        "status": 400,
                    },
                    status=400,
                )

        send_withdrawal_notification_sms.delay(
            account.user.mobile_number, amount, account.balance
        )
        send_withdrawal_notification_email.delay(
            account.user.email, amount, account.balance
        )

        return JsonResponse(
            {
                "message": f"Transaction created successfully for {account_number} account for {amount} amount",
                "status": 200,
            }
        )

    except json.JSONDecodeError:
        return JsonResponse(
            {
                "message": "Invalid JSON",
                "status": 400,
            },
            status=400,
        )
