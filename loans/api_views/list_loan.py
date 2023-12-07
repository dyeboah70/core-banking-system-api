from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from managers.decorators import check_permission
from loans.models import Loan


@csrf_exempt
@check_permission("view")
def list_loans(request):
    loans = Loan.objects.all().values(
        "id",
        "borrower__first_name",
        "borrower__last_name",
        "borrower__ghana_card_number",
        "borrower__mobile_number",
        "amount",
        "loan_type__name",
        "interest_amount",
        "amount_to_pay",
        "date_applied",
        "approved",
    )

    response_data = {
        "message": "loans listed successfully",
        "status": 200,
        "data": list(loans),
    }

    return JsonResponse(response_data, safe=False)
