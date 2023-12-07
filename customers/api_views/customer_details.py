from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from managers.decorators import check_permission
from accounts.models import Accounts
import json


@csrf_exempt
@require_POST
@check_permission("view")
def customer_details(request):
    try:
        data = json.loads(request.body)
        account_number = data.get("account_number")

        if account_number == "":
            return JsonResponse(
                {
                    "message": "Account number is required.",
                    "status": 400
                },
                status=400)

        account = Accounts.objects.get(account_number=account_number)
        profile = account.user

        message = "Customer details found"
        response_data = {
            "message": message,
            "status": 200,
            "data": {
                "profile_id": profile.profile_id,
                "balance": account.balance,
                "email": profile.email,
                "first_name": profile.first_name,
                "last_name": profile.last_name,
                "ghana_card_number": profile.ghana_card_number,
                "phone_number": profile.mobile_number,
                "occupation": profile.occupation,
                "date_of_birth": profile.date_of_birth,
                "city": profile.city,
                "postal_address": profile.postal_address,
                "sex": profile.sex,
                "marital_status": profile.marital_status,
                "account_number": account.account_number,
                "next_of_kin_name": account.user.next_of_kin_name,
                "next_of_kin_phone_number":
                account.user.next_of_kin_phone_number,
                "next_of_kin_address": account.user.next_of_kin_address,
                "next_of_kin_relationship":
                account.user.next_of_kin_relationship
            },
        }

        return JsonResponse(response_data, safe=False)

    except json.JSONDecodeError:
        return JsonResponse(
            {
                "message":
                "JSONDecodeError, You might have forgotten to provide your data / field(s) in json format.",
                "status": 400,
            },
            status=400,
        )

    # except Customers.DoesNotExist:
    #     return JsonResponse(
    #         {
    #             "message": "Customer details not found",
    #             "status": 404,
    #         },
    #         status=404,
    #     )
    #
    except Accounts.DoesNotExist:
        return JsonResponse({
            "message": "Account details not found",
            "status": 404,
        })
