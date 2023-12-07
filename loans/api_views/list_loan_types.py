from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from managers.decorators import check_permission
from loans.models import LoanType


@csrf_exempt
@check_permission("view")
def list_loan_types(request):
    loans = LoanType.objects.all().values(
        "id",
        "name",
    )

    response_data = {
        "message": "loan types listed successfully",
        "status": 200,
        "data": list(loans),
    }

    return JsonResponse(response_data, safe=False)
