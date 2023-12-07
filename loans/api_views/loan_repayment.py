from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from managers.decorators import check_permission
from django.views.decorators.http import require_http_methods
from loans.models import Loan, Repayment
from customers.models import Customers
from transactions.decorators import is_teller
import json


@csrf_exempt
@require_http_methods(["POST"])
@check_permission("transaction")
@is_teller
def loan_repayment(request, teller=None):
    try:
        data = json.loads(request.body)
        amount = data.get("amount")
        ghana_card_number = data.get("ghana_card_number")

        if any(item == "" for item in [amount, ghana_card_number]) is None:
            return JsonResponse(
                {
                    "message": "Missing parameters in request",
                    "status": 400,
                },
                status=400,
            )

        # customer
        try:
            customer = Customers.objects.get(
                ghana_card_number=ghana_card_number)

        except Customers.DoesNotExist:
            return JsonResponse(
                {
                    "message": "Customer not found",
                    "status": 404,
                },
                status=404,
            )

        # loan
        try:
            loan = Loan.objects.get(borrower=customer)
            repayment = Repayment.objects.create(loan=loan, amount=amount)
            repayment.teller_id = teller.profile_id
            repayment.save()

            # Repayment.calculate_repayments(loan)

        except Loan.DoesNotExist:
            return JsonResponse(
                {
                    "message": "Loan not found",
                    "status": 404,
                },
                status=404,
            )

        except Repayment.DoesNotExist:
            return JsonResponse(
                {
                    "message": "Repayment not found",
                    "status": 404,
                },
                status=404,
            )

        # Repayment

        response_data = {
            "message": "Repayment created successfully",
            "status": 200,
            "data": {
                "ghana_card_number": ghana_card_number,
                "amount": amount
            }
        }

        return JsonResponse(response_data, content_type="application/json")

    except Exception as e:
        return JsonResponse({
            "message": f"An error occurred: {str(e)}",
            "status": 500
        })
