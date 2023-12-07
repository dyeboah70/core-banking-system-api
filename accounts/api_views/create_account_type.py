from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from managers.decorators import check_permission
from accounts.models import AccountTypes
import json
from django.views.decorators.http import require_POST


@check_permission("add")
@require_POST
@csrf_exempt
def create_account_type(request):
    try:
        data = json.loads(request.body)
        account_type = data.get("account_type")
        maximum_withdrawal_amount = data.get("maximum_withdrawal_amount")
        annual_interest_rate = data.get("annual_interest_rate")
        interest_calculation_per_year = data.get(
            "interest_calculation_per_year")

        if any(item is None for item in [account_type, maximum_withdrawal_amount, annual_interest_rate, interest_calculation_per_year]):
            return JsonResponse(
                {
                    "message": "Missing parameters in request, account_type, maximum_withdrawal_amount, annual_interest_rate, interest_calculation_per_year",
                    "status": 400,
                },
                status=400,
            )

        account_type = AccountTypes.objects.create(
            account_type=account_type,
            maximum_withdrawal_amount=maximum_withdrawal_amount,
            annual_interest_rate=annual_interest_rate,
            interest_calculation_per_year=interest_calculation_per_year
        )

        return JsonResponse(
            {
                "message": "Account type created successfully",
                "status": 200,
                "data": {
                    "id": account_type.id,
                    "account_type": account_type.account_type,
                    "maximum_withdrawal_amount": account_type.maximum_withdrawal_amount,
                    "annual_interest_rate": account_type.annual_interest_rate,
                    "interest_calculation_per_year": account_type.interest_calculation_per_year,
                }
            },
            status=200,
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
                "message": f"Failed to create account type: {str(e)}",
                "status": 500,
            },
            status=500,
        )
