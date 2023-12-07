from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from managers.decorators import check_permission
from customers.models import Customers
from django.views.decorators.http import require_POST
from loans.models import Loan, Repayment, LoanType
from django.db.models import Sum


@csrf_exempt
@require_POST
@check_permission("transaction")
def create_loan(request):
    try:
        data = json.loads(request.body)
        ghana_card_number = data.get("ghana_card_number")
        amount = data.get("amount")
        loan_type = data.get("loan_type")

        if any(item is None for item in [ghana_card_number, amount, loan_type]):
            return JsonResponse(
                {
                    "message": "Missing parameters in request, ghana_card_number, amount, loan_type",
                    "status": 400,
                },
                status=400,
            )

        loan_type = LoanType.objects.get(id=int(loan_type))

        # check if user is owing a loan
        user_loan = Loan.objects.filter(borrower__ghana_card_number=ghana_card_number).aggregate(
            total_amount=Sum("amount_to_pay"))

        repayments = Repayment.objects.filter(
            loan__borrower__ghana_card_number=ghana_card_number).aggregate(
            total_repayments=Sum("amount"))

        if (user_loan["total_amount"] is not None
            and repayments["total_repayments"] is not None
                and repayments["total_repayments"] != user_loan["total_amount"]):
            # calculate the amount remaining
            amount_remaining = user_loan["total_amount"] - \
                repayments["total_repayments"]

            return JsonResponse(
                {
                    "message": f"User with ghana_card_number {ghana_card_number} is owing a loan with amount {amount_remaining} remaining",
                    "status": 400,
                },
                status=400,
            )
        elif user_loan["total_amount"] is not None:
            amount_remaining = user_loan["total_amount"]

            return JsonResponse(
                {
                    "message": f"User with ghana_card_number {ghana_card_number} is owing a loan with amount {amount_remaining} remaining",
                    "status": 400,
                }
            )

        borrower = Customers.objects.get(ghana_card_number=ghana_card_number)
        loan = Loan.objects.create(
            borrower=borrower,
            amount=amount,
            loan_type=loan_type,
        )
        loan.interest_amount = loan.calculate_interest(loan.amount)
        loan.amount_to_pay = loan.interest_amount + amount
        loan.save()

        return JsonResponse(
            {
                "message": "Loan created successfully",
                "status": 200,
                "data": {
                    "profile_id": loan.borrower.profile_id,
                    "first_name": loan.borrower.first_name,
                    "last_name": loan.borrower.last_name,
                    "ghana_card_number": loan.borrower.ghana_card_number,
                    "mobile_number": loan.borrower.mobile_number,
                    "amount": loan.amount,
                    "interest_amount": loan.interest_amount,
                    "amount_to_pay": loan.amount_to_pay,
                    "date_applied": loan.date_applied,
                    "loan_type": loan.loan_type.name
                }
            },
            status=200,
        )

    except Customers.DoesNotExist:
        return JsonResponse(
            {
                "message": f"User with ghana_card_number {ghana_card_number} does not exist",
                "status": 404,
            },
            status=404,
        )

    except LoanType.DoesNotExist:
        return JsonResponse(
            {
                "message": f"Loan type with id {loan_type} does not exist",
                "status": 404,
            },
            status=404,
        )

    except json.JSONDecodeError:
        return JsonResponse(
            {
                "message": "Missing parameters in request, ghana_card_number, amount, loan_type",
                "status": 400,
            },
            status=400,
        )

    except Repayment.DoesNotExist:
        return JsonResponse(
            {
                "message": "Missing parameters in request, ghana_card_number, amount, loan_type",
                "status": 400,
            }
        )

    except Exception as e:
        return JsonResponse(
            {
                "message": f"Failed to create loan: {str(e)}",
                "status": 500,
            },
            status=500,
        )
