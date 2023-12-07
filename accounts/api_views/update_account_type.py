from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from accounts.models import AccountTypes
from managers.decorators import check_permission
from django.views.decorators.http import require_http_methods


@csrf_exempt
@check_permission("add")
@require_http_methods(["POST"])
def update_account_type(request, account_type_id):
    try:
        account_type = AccountTypes.objects.get(id=account_type_id)

        data = json.loads(request.body)
        account_type_value = data.get("account_type")
        maximum_withdrawal_amount = data.get("maximum_withdrawal_amount")
        annual_interest_rate = data.get("annual_interest_rate")
        interest_calculation_per_year = data.get(
            "interest_calculation_per_year")

        if any(item is None for item in [account_type_value, maximum_withdrawal_amount, annual_interest_rate, interest_calculation_per_year]):
            return JsonResponse(
                {
                    "message": "Missing parameters in request, account_type, maximum_withdrawal_amount, annual_interest_rate, interest_calculation_per_year",
                    "status": 400,
                },
                status=400,
            )

        account_type.account_type = account_type_value
        account_type.maximum_withdrawal_amount = maximum_withdrawal_amount
        account_type.annual_interest_rate = annual_interest_rate
        account_type.interest_calculation_per_year = interest_calculation_per_year
        account_type.save()

        return JsonResponse(
            {
                "message": "Account type updated successfully",
                "status": 200,
                "data": {
                    "id": account_type.id,
                    "account_type": account_type.account_type,
                    "maximum_withdrawal_amount": account_type.maximum_withdrawal_amount,
                    "annual_interest_rate": account_type.annual_interest_rate,
                    "interest_calculation_per_year": account_type.interest_calculation_per_year
                }
            },
            status=200,
        )

    except AccountTypes.DoesNotExist:
        return JsonResponse(
            {
                "message": f"Account type with id {account_type_id} does not exist",
                "status": 404,
            },
            status=404,
        )

    except json.JSONDecodeError:
        return JsonResponse(
            {
                "message": "Missing parameters in request, account_type, maximum_withdrawal_amount, annual_interest_rate, interest_calculation_per_year",
                "status": 400,
            },
            status=400,
        )

    except Exception as e:
        return JsonResponse(
            {
                "message": f"Failed to update account type: {str(e)}",
                "status": 500,
            },
            status=500,
        )
