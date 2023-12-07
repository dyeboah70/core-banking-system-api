from django.http import JsonResponse
from managers.utils import get_user_from_token
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from json import JSONDecodeError
from managers.decorators import check_permission

import json


@csrf_exempt
@require_POST
@check_permission("view")
def verify_token(request):
    try:
        data = json.loads(request.body)
        token = data.get("token")

        if not token:
            return JsonResponse(
                {"message": "Token not provided", "status": 401}, status=401
            )

        user = get_user_from_token(token)

        if user is None:
            return JsonResponse({"message": "Invalid token", "status": 401}, status=401)

        message = "Token verified"

        response_data = {
            "message": message,
            "status": 200,
            "data": {
                "profile_id": user.profile_id,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "staff_id": user.staff_id,
                "phone_number": user.phone_number,
                "roles": [role.name for role in user.roles.all()]
                if user.roles.exists()
                else None,
            },
        }
        return JsonResponse(response_data, content_type="application/json")

    except JSONDecodeError:
        return JsonResponse(
            {
                "message": "JSONDecodeError: Invalid or missing JSON data in the request body",
                "status": 400,
            },
            status=400,
        )
