from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from managers.models import Managers
from django.views.decorators.http import require_POST
from managers.decorators import check_permission
import json


@csrf_exempt
@require_POST
@check_permission("view")
def staff_details(request):
    try:
        data = json.loads(request.body)
        profile_id = data.get("profile_id")

        if profile_id == "":
            return JsonResponse(
                {"message": "Profile id is required.", "status": 400}, status=400
            )

        profile = Managers.objects.get(profile_id=profile_id)

        message = "Staff details found"
        response_data = {
            "message": message,
            "status": 200,
            "data": {
                "profile_id": profile.profile_id,
                "email": profile.email,
                "first_name": profile.first_name,
                "last_name": profile.last_name,
                "staff_id": profile.staff_id,
                "phone_number": profile.phone_number,
                "roles": [role.name for role in profile.roles.all()]
                if profile.roles.exists()
                else None,
            },
        }

        return JsonResponse(response_data, safe=False)

    except json.JSONDecodeError:
        return JsonResponse(
            {
                "message": "JSONDecodeError, You might have forgotten to provide your data / field(s) in json format.",
                "status": 400,
            },
            status=400,
        )

    except Managers.DoesNotExist:
        return JsonResponse(
            {
                "message": "Staff details not found",
                "status": 404,
            },
            status=404,
        )
