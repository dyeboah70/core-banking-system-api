from functools import wraps
from django.http import JsonResponse
from managers.utils import get_user_from_token
from django.core.exceptions import ValidationError
from managers.models import Managers


def is_teller(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        token = request.headers.get("Authorization", "").split(" ")[-1]

        if not token:
            return JsonResponse(
                {"message": "Authorization header not provided.", "status": 400},
                status=400,
            )

        try:
            user = get_user_from_token(token)
            teller = Managers.objects.get(email=user)

        except ValidationError as e:
            return JsonResponse({"message": "Invalid token", "status": 401}, status=401)

        except Managers.DoesNotExist:
            return JsonResponse(
                {"message": "User is not a seller.", "status": 401}, status=401
            )

        kwargs["teller"] = teller  # Pass the seller object to the view function

        return func(request, *args, **kwargs)

    return wrapper
