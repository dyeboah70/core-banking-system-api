from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from managers.decorators import check_permission
from loans.models import LoanType
from django.views.decorators.http import require_http_methods


@csrf_exempt
@check_permission("add")
@require_http_methods(["POST"])
def update_loan_type(request, loan_type_id):
    try:
        loan_type = LoanType.objects.get(id=loan_type_id)

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

        loan_type.name = name
        loan_type.annual_interest_rate = annual_interest_rate
        loan_type.interest_calculation_per_year = interest_calculation_per_year
        loan_type.save()

        return JsonResponse(
            {
                "message": "Loan type updated successfully",
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

    except LoanType.DoesNotExist:
        return JsonResponse(
            {
                "message": f"Loan type with id {loan_type_id} does not exist",
                "status": 404,
            },
            status=404,
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
                "message": f"Failed to update loan type: {str(e)}",
                "status": 500,
            },
            status=500,
        )
