from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.http import JsonResponse
from managers.tasks import send_password_manager_email
from django.views.decorators.csrf import csrf_exempt
import json
from managers.models import Managers


@csrf_exempt
def password_reset_request_view(request):
    """
    Handles a password reset request.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: The JSON response containing the result of the password reset request.

    Raises:
        None
    """
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            email = data.get("email")
        except json.JSONDecodeError:
            return JsonResponse(
                {
                    "message": "JSONDecodeError, You might have forgotten to provide your data / field(s) in json format.",
                    "status": 400,
                },
                status=400,
            )

        if email == "":
            return JsonResponse(
                {"message": "Email is required.", "status": 400}, status=400
            )

        try:
            validate_email(email)
        except ValidationError:
            return JsonResponse(
                {"message": "Invalid email address.", "status": 400}, status=400
            )

        try:
            user = Managers.objects.get(email=email)

        except Managers.DoesNotExist:
            return JsonResponse(
                {"message": "User does not exist.", "status": 404}, status=404
            )
        if user:
            send_password_manager_email.delay(user.id)
            return JsonResponse(
                {"message": f"Password reset email sent to {email}.", "status": 200},
                status=200,
            )
        else:
            return JsonResponse(
                {"message": "User does not exist.", "status": 404}, status=404
            )
    else:
        return JsonResponse(
            {"message": "Invalid request method.", "status": 405}, status=405
        )
