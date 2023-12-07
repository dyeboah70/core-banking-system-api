from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from managers.decorators import check_permission
from accounts.models import Accounts
from customers.models import Customers
from django.views.decorators.http import require_POST
import json


@csrf_exempt
@check_permission("view")
@require_POST
def get_account_data(request):
    try:
        data = json.loads(request.body)
        customer_ghana_card = data.get("customer_ghana_card")

        customer = Customers.objects.get(ghana_card_number=customer_ghana_card)

        accounts = Accounts.objects.select_related("account_type").filter(user=customer).values(
            "account_number",
            "account_type__account_type",
            "user__first_name",
            "user__last_name",
            "user__email",
            "user__mobile_number"
        )

        account_data_list = list(accounts)
        transform_account_data = [{
            "account_number": account["account_number"],
            "account_type": account["account_type__account_type"],
            "first_name": account["user__first_name"],
            "last_name": account["user__last_name"],
            "email": account["user__email"],
            "mobile_number": account["user__mobile_number"]
        } for account in accounts]

        if account_data_list:
            response_data = {
                "message": "Account data listed successfully",
                "status": 200,
                "data": transform_account_data,
            }
        else:
            response_data = {
                "message": "No accounts found for the customer",
                "status": 404,
            }

        return JsonResponse(response_data, safe=False)

    except json.decoder.JSONDecodeError:
        response_data = {
            "message": "Invalid data format",
            "status": 400,
        }

        return JsonResponse(response_data, safe=False)

    except Customers.DoesNotExist:
        response_data = {
            "message": "Customer does not exist",
            "status": 404,
        }

        return JsonResponse(response_data, safe=False)
