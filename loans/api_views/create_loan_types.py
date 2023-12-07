from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from managers.decorators import check_permission
from loans.models import LoanType


@csrf_exempt
@check_permission("add")
def create_loan_type(request):
    try:
        data = json.loads(request.body)
        name = data.get("name")
        annual_interest_rate = data.get("annual_interest_rate")
        interest_calculation_per_year = data.get(
            "interest_calculation_per_year")

        if any(item is None for item in [name, annual_interest_rate,
                                         interest_calculation_per_year]):
            return JsonResponse(
                {
                    "message": "Missing parameters in request, name, annual_interest_rate, interest_calculation_per_year",
                    "status": 400,
                },
                status=400,
            )

        loan_type = LoanType.objects.create(
            name=name,
            annual_interest_rate=annual_interest_rate,
            interest_calculation_per_year=interest_calculation_per_year
        )

        return JsonResponse(
            {
                "message": "Loan type created successfully",
                "status": 200,
                "data": {
                    "id": loan_type.id,
                    "name": loan_type.name,
                    "annual_interest_rate": loan_type.annual_interest_rate,
                    "interest_calculation_per_year": loan_type.interest_calculation_per_year
                }
            },
            status=200,
        )

    except json.JSONDecodeError:
        return JsonResponse(
            {
                "message": "Missing parameters in request, name, annual_interest_rate, interest_calculation_per_year",
                "status": 400,
            },
            status=400,
        )

    except Exception as e:
        return JsonResponse(
            {
                "message": f"Failed to create loan type: {str(e)}",
                "status": 500,
            },
            status=500,
        )
