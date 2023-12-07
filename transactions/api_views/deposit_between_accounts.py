from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json
from managers.decorators import check_permission
from transactions.decorators import is_teller
from accounts.models import Accounts
from transactions.models import Transactions
from managers.tasks import send_deposit_notification_email


@csrf_exempt
@require_POST
@check_permission("transaction")
@is_teller
def create_transaction_between_accounts(request, teller=None):
    try:
        data = json.loads(request.body)
        amount = data.get("amount")
        from_account_number = data.get("from_account_number")
        to_account_number = data.get("to_account_number")

        if any(item == ""
               for item in [amount, from_account_number, to_account_number]):
            return JsonResponse(
                {
                    "message": "Missing parameters in request",
                    "status": 400,
                },
                status=400,
            )

        if from_account_number == to_account_number:
            return JsonResponse(
                {
                    "message": "Cannot transfer money to the same account",
                    "status": 400,
                },
                status=400,
            )

        # Get the accounts
        try:
            debit_account = Accounts.objects.get(
                account_number=from_account_number)
            credit_account = Accounts.objects.get(
                account_number=to_account_number)

            if debit_account.balance < amount:
                return JsonResponse(
                    {
                        "message": "Insufficient balance in the debit account",
                        "status": 400,
                    },
                    status=400,
                )

            transaction = Transactions.objects.create(
                user=debit_account.user,
                amount=amount,
                teller_id=teller.profile_id,
                account_number=debit_account.account_number,
            )

            debit_account.balance -= amount
            debit_account.save()

            credit_account.balance += amount
            credit_account.save()

            send_deposit_notification_email.delay(credit_account.user.email,
                                                  amount,
                                                  credit_account.balance)

            return JsonResponse({
                "message":
                f"Transaction created successfully from account {from_account_number} to account {to_account_number} for {amount} amount",
                "status": 200,
            })

        except Accounts.DoesNotExist:
            return JsonResponse(
                {
                    "message": "One or both accounts do not exist",
                    "status": 400,
                },
                status=400,
            )

    except json.decoder.JSONDecodeError:
        return JsonResponse(
            {
                "message": "Invalid JSON",
                "status": 400,
            },
            status=400,
        )
