from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from managers.decorators import check_permission
from customers.models import Customers
from accounts.models import Accounts
from django.views.decorators.http import require_http_methods


@csrf_exempt
@require_http_methods(["POST"])
@check_permission("add_customer")
def update_customer(request, profile_id):
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

        # Update the customer's profile fields based on the provided data
        customer.mobile_number = data.get("mobile_number",
                                          customer.mobile_number)
        customer.occupation = data.get("occupation", customer.occupation)
        customer.first_name = data.get("first_name", customer.first_name)
        customer.last_name = data.get("last_name", customer.last_name)
        customer.ghana_card_number = data.get("ghana_card_number",
                                              customer.ghana_card_number)
        customer.date_of_birth = data.get("date_of_birth",
                                          customer.date_of_birth)
        customer.city = data.get("city", customer.city)
        customer.postal_address = data.get("postal_address",
                                           customer.postal_address)
        customer.sex = data.get("sex", customer.sex)
        customer.marital_status = data.get("marital_status",
                                           customer.marital_status)
        customer.next_of_kin_name = data.get("next_of_kin_name",
                                             customer.next_of_kin_name)
        customer.next_of_kin_phone_number = data.get(
            "next_of_kin_phone_number", customer.next_of_kin_phone_number)
        customer.next_of_kin_address = data.get("next_of_kin_address",
                                                customer.next_of_kin_address)
        customer.next_of_kin_relationship = data.get(
            "next_of_kin_relationship", customer.next_of_kin_relationship)
        customer.email = data.get("email", customer.email)
        account.account_number = data.get("account_number",
                                          account.account_number)

        customer.save()
        account.save()

        response_data = {
            "message": "Customer profile updated successfully",
            "status": 200,
            "data": {
                "profile_id": customer.profile_id,
                "account_number": account.account_number,
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
    except Exception as e:
        # Handle other exceptions if needed
        return JsonResponse(
            {
                "message": "An error occurred: " + str(e),
                "status": 500
            },
            status=500)
