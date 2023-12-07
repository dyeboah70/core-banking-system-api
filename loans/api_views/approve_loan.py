from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from managers.decorators import check_permission
from django.views.decorators.http import require_http_methods
from loans.models import Loan
from managers.tasks import send_loan_approved_sms


@csrf_exempt
@require_http_methods(["POST"])
@check_permission("approve_account")
def approve_loan(request, id):
    try:
        data = json.loads(request.body)
        status = data.get("status")

        loan = Loan.objects.get(id=id)

        loan.approved = status
        loan.save()

        response_data = {
            "message": "Loan status updated successfully",
            "status": 200,
            "data": {
                "profile_id": loan.borrower.profile_id,
                "first_name": loan.borrower.first_name,
                "last_name": loan.borrower.last_name,
                "ghana_card_number": loan.borrower.ghana_card_number,
                "mobile_number": loan.borrower.mobile_number,

            },

        }

        if status:
            send_loan_approved_sms.delay(loan.borrower.mobile_number)

        return JsonResponse(response_data, content_type="application/json")

    except json.JSONDecodeError:
        return JsonResponse(
            {
                "message": "status is required.",
                "status": 400,
            },
            status=400)

    except Loan.DoesNotExist:
        return JsonResponse(
            {
                "message": f"Loan with id {id} does not exist",
                "status": 404,
            },
            status=404)
