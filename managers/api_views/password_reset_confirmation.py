from django.http import JsonResponse
from managers.utils import validate_token
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def password_reset_confirm_view(request, token):
    if request.method == "GET":
        user, is_valid_token = validate_token(token)
        if not is_valid_token:
            return JsonResponse({"message": "Invalid token", "status": 400}, status=400)

        return JsonResponse(
            {"message": "Please enter your new password", "status": 200}, status=200
        )

    elif request.method == "POST":
        user, is_valid_token = validate_token(token)
        if not is_valid_token:
            return JsonResponse({"message": "Invalid token", "status": 400}, status=400)

        try:
            data = json.loads(request.body)
            password = data.get("password", "")
            confirm_password = data.get("confirm_password", "")
        except json.JSONDecodeError:
            return JsonResponse(
                {
                    "message": "JSONDecodeError, You might have forgotten to provide your data / field(s) in json format.",
                    "status": 400,
                },
                status=400,
            )

        if any(item == "" for item in [password, confirm_password]):
            return JsonResponse(
                {
                    "message": "Password and confirm password fields are required.",
                    "status": 400,
                },
                status=400,
            )

        user.set_password(password)
        user.password_reset_token = None
        user.password_reset_token_created_at = None
        user.save()

        return JsonResponse(
            {"message": f"Password changed {user.email}", "status": 200}, status=200
        )
