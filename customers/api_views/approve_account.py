from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from managers.decorators import check_permission
from customers.models import Customers
from accounts.models import Accounts
from django.views.decorators.http import require_http_methods
from managers.tasks import send_account_approved_sms


@csrf_exempt
@require_http_methods(["POST"])  # Only accept POST requests
@check_permission("approve_account")
def update_status(request, profile_id):
    try:
        try:
            customer = Customers.objects.get(profile_id=profile_id)
            account = Accounts.objects.get(user=customer)
        except Customers.DoesNotExist:
            return JsonResponse(
                {
                    "message": "Customer not found",
                    "status": 404
                }, status=404)

        data = json.loads(request.body)
        status = data.get("status")
        account.is_approved = status

        response_data = {
            "message": "Customer Account approved successfully",
            "status": 200,
            "data": {
                "profile_id": customer.profile_id,
                "email": customer.email,
                "first_name": customer.first_name,
                "last_name": customer.last_name,
                "ghana_card_number": customer.ghana_card_number,
                "mobile_number": customer.mobile_number,
                "occupation": customer.occupation,
                "date_of_birth": str(customer.date_of_birth),
                "city": customer.city,
                "postal_address": customer.postal_address,
                "sex": customer.sex,
                "marital_status": customer.marital_status,
                "next_of_kin_name": customer.next_of_kin_name,
                "next_of_kin_phone_number": customer.next_of_kin_phone_number,
                "next_of_kin_address": customer.next_of_kin_address,
                "next_of_kin_relationship": customer.next_of_kin_relationship,
            },
        }

        if status:
            send_account_approved_sms.delay(customer.mobile_number)

        return JsonResponse(response_data, content_type="application/json")

    except json.JSONDecodeError:
        return JsonResponse(
            {
                "message":
                "JSONDecodeError, You might have forgotten to provide your data/field(s) in JSON format.",
                "status": 400,
            },
            status=400,
        )

    except Customers.DoesNotExist:
        return JsonResponse(
            {
                "message": "Customer not found",
                "status": 404
            }, status=404)

    except Accounts.DoesNotExist:
        return JsonResponse(
            {
                "message": "Account not found",
                "status": 404
            }, status=404)

    except Exception as e:
        # Handle other exceptions if needed
        return JsonResponse(
            {
                "message": "An error occurred: " + str(e),
                "status": 500
            },
            status=500)
