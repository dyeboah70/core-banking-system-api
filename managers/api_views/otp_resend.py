from django.core.cache import cache
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from managers.utils import generate_and_send_verification_code, get_user_from_token
from django.views.decorators.http import require_POST
from django.core.exceptions import ValidationError


@csrf_exempt
@require_POST
def otp_code_resend_view(request):
    """
    Resends an OTP code to the user's email address.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response indicating the status of the OTP resend operation. If successful, the response will have a status code of 200 and a message indicating that the OTP has been resent. If there is an error, the response will have a status code of 400 and a corresponding error message.

    Raises:
        None.
    """
    # Get authorization header
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
        email = user.email
    except Exception:
        return JsonResponse({"message": "Invalid token", "status": 401}, status=401)

    # Generate a new OTP and store it in the cache
    cache.set(f"email_sent_time-{email}", timezone.now(), timeout=300)

    # Send the new OTP to the user's email using your email sending service
    generate_and_send_verification_code(email)

    return JsonResponse(
        {"message": f"OTP resent to {email}.", "status": 200}, status=200
    )
