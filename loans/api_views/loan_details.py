from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from managers.decorators import check_permission
import json
from loans.models import Loan, Repayment
from customers.models import Customers
from django.db.models import Sum


@csrf_exempt
@require_POST
@check_permission("view")
def loan_details(request):
    try:
        data = json.loads(request.body)
        ghana_card_number = data.get("ghana_card_number")

        if ghana_card_number == "":
            return JsonResponse(
                {
                    "message": "ghana_card_number is required.",
                    "status": 400
                },
                status=400)

        if any(item is None for item in [ghana_card_number]):
            return JsonResponse(
                {
                    "message": "ghana_card_number is required.",
                }
            )

        borrower = Customers.objects.get(ghana_card_number=ghana_card_number)

        loan = Loan.objects.get(borrower=borrower)

        repayment = Repayment.objects.filter(loan_id=loan.id)
        total_repaid = repayment.aggregate(
            total_repaid=Sum('amount'))['total_repaid']



        if total_repaid is None:
            total_repaid = 0


        amount_remaining = loan.amount_to_pay - total_repaid

        response_data = {
            "message": "Loan details found",
            "status": 200,
            "data": {
                "ghana_card_number": loan.borrower.ghana_card_number,
                "mobile_number": loan.borrower.mobile_number,
                "first_name": loan.borrower.first_name,
                "last_name": loan.borrower.last_name,
                "loan_amount": loan.amount,
                "interest_amount": loan.interest_amount,
                "amount_to_pay": loan.amount_to_pay,
                "total_repaid": total_repaid,
                "amount_remaining": amount_remaining,
                "date_applied": loan.date_applied,

            }
        }

        return JsonResponse(response_data, safe=False)

    except json.JSONDecodeError:
        return JsonResponse(
            {
                "message": "ghana_card_number is required.",
                "status": 400
            },
            status=400)

    except Loan.DoesNotExist:
        return JsonResponse(
            {
                "message": f"Loan with ghana_card_number {ghana_card_number} does not exist",
                "status": 404
            },
            status=404)

    except Customers.DoesNotExist:
        return JsonResponse(
            {
                "message": f"Customer with ghana_card_number {ghana_card_number} does not exist",
                "status": 404
            },
            status=404)
