from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from managers.decorators import check_permission
from accounts.models import Accounts
from django.views.decorators.http import require_POST
import json


@csrf_exempt
@check_permission("view")
@require_POST
def verify_account_number(request):
    data = json.loads(request.body)
    account_number = data.get("account_number")

    if account_number is None:
        return JsonResponse(
            {"message": "account_number is required"}
        )
    try:
        account = Accounts.objects.get(account_number=account_number)
    except Accounts.DoesNotExist:
        return JsonResponse(
            {
                "message": "Account not found",
                "status": 404
            }, status=404)
    
    except json.JSONDecodeError:
        return JsonResponse(
            {
                "message": "Invalid JSON",
                "status": 400
            }, status=400)
    
    except Exception as e:
        return JsonResponse(
            {
                "message": f"Something went wrong: {e}",
                "status": 500
            }, status=500)

    response_data = {
        "message": "Account verified successfully",
        "status": 200,
        "data": {
            "account_number": account.account_number,
            "account_type": account.account_type.account_type,
            "first_name": account.user.first_name,
            "last_name": account.user.last_name,
            "email": account.user.email,
            "mobile_number": account.user.mobile_number
            },
        }

    

    return JsonResponse(response_data, content_type="application/json", safe=False)
