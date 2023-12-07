from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from managers.models import Managers
from managers.tasks import send_user_password
from managers.utils import create_random_password
from django.conf import settings
from managers.models import Roles
from django.db.utils import IntegrityError
import json
from managers.models import Permission
from managers.decorators import check_permission
from django.core.exceptions import ValidationError


@csrf_exempt
@require_POST
@check_permission("add_user")
def create_staff(request):
    try:
        data = json.loads(request.body)
        email = data.get("email")
        staff_id = data.get("staff_id")
        phone_number = data.get("phone_number")
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        role_names = data.get("role_name")

        # Validate required parameters
        if any([
                not email, not staff_id, not phone_number, not first_name,
                not last_name, not role_names
        ]):
            return JsonResponse(
                {
                    "message": "Missing parameters in request",
                    "status": 400,
                },
                status=400,
            )

        # Convert single role name to a list
        if not isinstance(role_names, list):
            role_names = [role_names]

        # Fetch valid role IDs and check for invalid roles
        role_ids = list(Roles.objects.values_list("id", flat=True))
        invalid_roles = [
            role_id for role_id in role_names if role_id not in role_ids
        ]
        if invalid_roles:
            return JsonResponse(
                {
                    "message":
                    "Invalid role ID(s): " +
                    ", ".join(map(str, invalid_roles)),
                    "status":
                    400,
                },
                status=400,
            )

        # Get or create the user
        user, created = Managers.objects.get_or_create(
            email=email,
            defaults={
                "first_name": first_name,
                "last_name": last_name,
                "staff_id": staff_id,
                "phone_number": phone_number,
            },
        )

        if not created:
            return JsonResponse(
                {
                    "message": "User not created / already exists",
                    "status": 400
                },
                status=400,
            )

        # Set user password
        password = create_random_password()
        user.set_password(password)
        user.save()

        # Set user roles and permissions
        user.roles.set(Roles.objects.filter(id__in=role_names))
        if settings.IT_MANAGER_ROLE in role_names:
            user.user_permissions.set(
                Permission.objects.exclude(
                    name__in=["add_customer", "transaction", "view"]))
        elif settings.TELLER_ROLE in role_names:
            user.user_permissions.set(
                Permission.objects.exclude(name="add_user"))
        elif settings.MANAGER_ROLE in role_names:
            user.user_permissions.set(
                Permission.objects.exclude(name="add_user"))
        elif settings.CUSTOMER_SERVICE_ROLE in role_names:
            user.user_permissions.set(
                Permission.objects.exclude(name="transaction"))

        send_user_password.delay(password=password, email=email)
        message = "Please check your email for your credentials"

        response_data = {
            "message": message,
            "status": 200,
            "data": {
                "profile_id":
                user.profile_id,
                "email":
                user.email,
                "first_name":
                user.first_name,
                "last_name":
                user.last_name,
                "staff_id":
                user.staff_id,
                "phone_number":
                user.phone_number,
                "role": [role.name for role in user.roles.all()]
                if user.roles.exists() else None,
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
    except IntegrityError as e:
        return JsonResponse(
            {
                "message": "Service ID already exists",
                "status": 400
            },
            status=400,
        )
    except ValidationError as e:
        return JsonResponse(
            {
                "message": str(e),
                "status": 400
            },
            status=400,
        )
    except Exception as e:
        return JsonResponse(
            {
                "message": "An error occurred: " + str(e),
                "status": 500
            },
            status=500,
        )
