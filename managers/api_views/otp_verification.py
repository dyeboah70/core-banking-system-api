from django.core.cache import cache
from django.contrib.auth import login
from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.conf import settings
from managers.utils import get_user_from_token, generate_token
from django.core.exceptions import ValidationError
import json


@csrf_exempt
@require_POST
def otp_verification_view(request):
    """
    View function for OTP verification.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: The JSON response containing the result of the OTP verification.
    """

    # Get the token from the request headers
    token = request.headers.get("Authorization", "").split(" ")[-1]

    if not token:
        return JsonResponse(
            {"message": "Authorization header not provided.", "status": 400}, status=400
        )
    try:
        user = get_user_from_token(token)

    except ValidationError as e:
        return JsonResponse({"message": "Invalid token", "status": 401}, status=401)

    try:
        data = json.loads(request.body)
        otp = data.get("otp")
    except json.JSONDecodeError:
        return JsonResponse(
            {
                "message": "JSONDecodeError, You might have forgotten to provide your data / field(s) in json format.",
                "status": 400,
            },
            status=400,
        )

    if otp == "":
        return JsonResponse({"message": "otp is required", "status": 400}, status=400)

    try:
        email = user.email
    except Exception:
        return JsonResponse({"message": "Invalid token", "status": 401}, status=401)

    # Verify the OTP
    email_cache_key = f"email-{email}"
    code = cache.get(email_cache_key)
    print(code)
    if code != otp:
        return JsonResponse(
            {"message": "Invalid OTP provided.", "status": 400}, status=400
        )

    otp_expiration_time = settings.OTP_EXPIRATION_TIME
    current_time = timezone.now()
    sent_time = cache.get(f"email_sent_time-{email}")
    if sent_time is None or (current_time - sent_time).seconds > otp_expiration_time:
        return JsonResponse(
            {
                "error": "OTP has expired. Please request for a new code.",
                "status": 400,
            },
            status=400,
        )

    # Delete the OTP key from cache once verified
    cache.delete(email_cache_key)

    token = generate_token(user)

    login(request, user, backend="Managers.custom_backend.AuthenticateManagers")
    return JsonResponse(
        {
            "message": f"OTP verified for {email}. User logged in.",
            "status": 200,
            "data": {
                "profile_id": user.profile_id,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "staff_id": user.staff_id,
                "phone_number": user.phone_number,
                "roles": [role.name for role in user.roles.all()],
                "token": token,
            },
        },
        status=200,
    )
