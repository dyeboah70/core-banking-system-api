from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from managers.decorators import check_permission
from django.views.decorators.http import require_http_methods
from loans.models import Loan, Repayment
from django.db.models import Sum


@csrf_exempt
@require_http_methods(["GET"])  # Only accept GET requests
@check_permission("view")
def has_user_finished_paying_loan(request, id):
    try:
        loan_exists = Loan.objects.filter(id=id).exists()

        if not loan_exists:
            return JsonResponse({
                "message": f"Loan with id {id} does not exist",
                "status": 404
            })

        repayments = Repayment.objects.filter(loan_id=id)
        total_repaid = repayments.aggregate(
            total_repaid=Sum('amount'))['total_repaid']

        if total_repaid is None:
            total_repaid = 0

        loan = Loan.objects.get(id=id)
        amount_remaining = loan.amount_to_pay - total_repaid
        borrower_data = {
            "profile_id": loan.borrower.profile_id,
            "first_name": loan.borrower.first_name,
            "last_name": loan.borrower.last_name,
            "ghana_card_number": loan.borrower.ghana_card_number,
            "mobile_number": loan.borrower.mobile_number,
            "loan_amount": loan.amount,
            "amount_to_pay": loan.amount_to_pay,
            "amount_remaining": amount_remaining,
        }

        if total_repaid >= loan.amount_to_pay:
            response_data = {
                "message": "Loan has been fully paid",
                "status": 200,
                "data": borrower_data
            }

        else:
            response_data = {
                "message": "Loan has not been fully paid",
                "status": 200,
                "data": borrower_data
            }

        return JsonResponse(response_data, content_type="application/json")

    except Exception as e:
        return JsonResponse({
            "message": f"An error occurred: {str(e)}",
            "status": 500
        })
