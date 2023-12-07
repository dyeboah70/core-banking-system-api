from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.utils import IntegrityError
from managers.decorators import check_permission
from customers.models import Customers
from managers.tasks import send_user_details_after_registration
from django.forms.models import model_to_dict
from accounts.models import AccountTypes, Accounts
from customers.utils import verify_ghana_card, verify_phone_number


@csrf_exempt
@require_POST
@check_permission("add_customer")
def create_customer(request):
    try:
        data = request.POST
        email = data.get("email")
        mobile_number = data.get("mobile_number")
        occupation = data.get("occupation")
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        ghana_card_number = data.get("ghana_card_number")
        date_of_birth = data.get("date_of_birth")
        city = data.get("city")
        postal_address = data.get("postal_address")
        sex = data.get("sex")
        marital_status = data.get("marital_status")
        next_of_kin_name = data.get("next_of_kin_name")
        next_of_kin_phone_number = data.get("next_of_kin_phone_number")
        next_of_kin_address = data.get("next_of_kin_address")
        next_of_kin_relationship = data.get("next_of_kin_relationship")
        account_type_id = data.get("account_type")
        image = request.FILES.get("image")

        if (
            any(
                item == ""
                for item in [
                    mobile_number,
                    occupation,
                    first_name,
                    last_name,
                    ghana_card_number,
                    date_of_birth,
                    city,
                    postal_address,
                    sex,
                    marital_status,
                    next_of_kin_name,
                    next_of_kin_phone_number,
                    next_of_kin_address,
                    next_of_kin_relationship,
                    account_type_id,
                    image,
                ]
            )
            is None
        ):
            return JsonResponse(
                {
                    "message": "Missing parameters in request",
                    "status": 400,
                },
                status=400,
            )

        if Customers.objects.filter(email=email).exists():
            return JsonResponse(
                {
                    "message": "User already exists",
                    "status": 400,
                },
                status=400,
            )

        if Customers.objects.filter(mobile_number=mobile_number).exists():
            return JsonResponse(
                {
                    "message": "Mobile number already exists",
                    "status": 400,
                },
                status=400,
            )
        
        if not verify_ghana_card(ghana_card_number):
            return JsonResponse(
                {
                    "message": "Ghana card number is invalid, please check again, eg. GHA-{9-digit number}-{digit}",
                    "status": 400,
                },
                status=400,
            )
        
        if not verify_phone_number(mobile_number) or not verify_phone_number(next_of_kin_phone_number):
            return JsonResponse(
                {
                    "message": "Mobile number is invalid, please check again, eg. 0572345678",
                    "status": 400,
                },
                status=400,
            )
 
        try:
            account_type = AccountTypes.objects.get(id=int(account_type_id))
        except AccountTypes.DoesNotExist:
            return JsonResponse(
                {
                    "message": "Account type does not exist",
                    "status": 400,
                },
                status=400,
            )

        if Customers.objects.filter(ghana_card_number=ghana_card_number).exists():
            return JsonResponse(
                {
                    "message": "Ghana card number already exists",
                    "status": 400,
                },
                status=400,
            )

        user, created = Customers.objects.get_or_create(
            email=email,
            defaults={
                "first_name": first_name,
                "last_name": last_name,
                "occupation": occupation,
                "mobile_number": mobile_number,
                "ghana_card_number": ghana_card_number,
                "date_of_birth": date_of_birth,
                "city": city,
                "postal_address": postal_address,
                "sex": sex,
                "marital_status": marital_status,
                "next_of_kin_name": next_of_kin_name,
                "next_of_kin_phone_number": next_of_kin_phone_number,
                "next_of_kin_address": next_of_kin_address,
                "next_of_kin_relationship": next_of_kin_relationship,
                "image": image,
            },
        )

        account = Accounts.objects.create(
            user=user,
            account_type=account_type,
        )
        account.save()

        if not created:
            return JsonResponse(
                {"message": "User not created / already exists", "status": 400},
                status=400,
            )

        user.save()

        message = "User created successfully"

        response_data = {
            "message": message,
            "status": 200,
            "data": {
                "profile_id": user.profile_id,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "ghana_card_number": user.ghana_card_number,
                "mobile_number": user.mobile_number,
                "occupation": user.occupation,
                "date_of_birth": str(user.date_of_birth),
                "city": user.city,
                "postal_address": user.postal_address,
                "sex": user.sex,
                "marital_status": user.marital_status,
                "next_of_kin_name": user.next_of_kin_name,
                "next_of_kin_phone_number": user.next_of_kin_phone_number,
                "next_of_kin_address": user.next_of_kin_address,
                "next_of_kin_relationship": user.next_of_kin_relationship,
                "account_type": account_type.account_type,
                "account_number": account.account_number,
                "image": user.image.url if user.image else None

            },
        }
        data = model_to_dict(user, exclude=["image"])
        send_user_details_after_registration.delay(data)  # send user details

        return JsonResponse(response_data, content_type="application/json")

    except IntegrityError as e:
        return JsonResponse(
            {"message": "User not created / already exists", "status": 400}, status=400
        )
    except Exception as e:
        return JsonResponse(
            {"message": "An error occurred: " + str(e), "status": 500}, status=500
        )
