from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from managers.decorators import check_permission
from accounts.models import Accounts, AccountTypes
from customers.models import Customers
from django.views.decorators.http import require_POST
import json


@csrf_exempt
@require_POST
@check_permission("add_customer")
def assign_account_to_customer(request):
    try:
        data = json.loads(request.body)
        customer_ghana_card = data.get("customer_ghana_card")
        account_type = data.get("account_type")

        account_type = AccountTypes.objects.get(id=int(account_type))
        customer = Customers.objects.get(ghana_card_number=customer_ghana_card)

        # Check if the user already has an account with the same account type
        existing_account = Accounts.objects.filter(
            user=customer, account_type=account_type
        ).first()
        if existing_account:
            response_data = {
                "message": "User already has an account with the same account type",
                "status": 400,
                "data": {
                    "account_number": existing_account.account_number,
                    "account_type": existing_account.account_type.account_type,
                    "first_name": existing_account.user.first_name,
                    "last_name": existing_account.user.last_name,
                    "email": existing_account.user.email,
                    "mobile_number": existing_account.user.mobile_number,
                },
            }
            return JsonResponse(response_data, status=400)

        account = Accounts.objects.create(account_type=account_type, user=customer)
        response_data = {
            "message": "Account assigned successfully",
            "status": 200,
            "data": {
                "account_number": account.account_number,
                "account_type": account.account_type.account_type,
                "first_name": account.user.first_name,
                "last_name": account.user.last_name,
                "email": account.user.email,
                "mobile_number": account.user.mobile_number,
            },
        }
        return JsonResponse(response_data, status=200)

    except AccountTypes.DoesNotExist:
        return JsonResponse(
            {"message": "Account type does not exist", "status": 404},
            status=404,
        )

    except Customers.DoesNotExist:
        return JsonResponse(
            {"message": "Customer does not exist", "status": 404},
            status=404,
        )

    except json.JSONDecodeError:
        return JsonResponse(
            {"message": "Invalid JSON", "status": 400},
            status=400,
        )
