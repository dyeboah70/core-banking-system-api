from django.contrib.auth.base_user import password_validation
from django.core.cache import cache
from django.utils import timezone
from managers.tasks import send_verification_email
from django.conf import settings
import jwt
from datetime import datetime, timedelta
import secrets
from django.utils.crypto import get_random_string
import random
import string
from celery.utils.log import get_logger

import threading

logger = get_logger(__name__)

lock = threading.Lock()


def generate_and_send_verification_code(email):
    """
    We have used lock to ensure that only one thread can access the cache at a time.
    The with lock statement acquires the lock before accessing the cache and releases it after the access is complete.
    This ensures that no two threads can access the cache at the same time, avoiding the race condition

    Generates and sends a verification code to the specified email address.

    Parameters:
        email (str): The email address to which the verification code will be sent.

    Returns:
        None
    """
    email_cache_key = f"email-{email}"
    code = "".join(secrets.choice(string.digits) for _ in range(6))

    with lock:
        cache.set(email_cache_key, code, timeout=300)
        cache.set(f"email_sent_time-{email}", timezone.now(), timeout=300)

    try:
        send_verification_email.delay(code=code, email=email)
    except send_verification_email.OperationalError as exc:
        logger.exception("Sending task raised: %r", exc)


def generate_managers_token(user):
    from managers.models import Managers

    expiration_time = datetime.utcnow() + timedelta(
        hours=settings.TOKEN_EXPIRATION_TIME
    )
    manager = Managers.objects.get(email=user.email)

    payload = {
        "user_id": str(manager.id),
        "roles": [role.name for role in manager.roles.all()]
        if manager.roles.exists()
        else None,
        "exp": expiration_time,
    }
    secret_key = settings.SECRET_KEY  # Replace with your own secret key
    algorithm = (
        settings.HASH_ALGORITHM
    )  # Choose the desired algorithm, such as 'HS256' or 'RS256'
    token = jwt.encode(payload, secret_key, algorithm)
    if not token:
        return {"message": "Error generating token", "status": 500}
    return token


def generate_token(user):
    """
    Generate a token for the given user.

    Parameters:
        user (User): The user for whom the token is generated.

    Returns:
        str: The generated token.

    This function generates a token for the given user by encoding a payload containing the user's ID, admin status, staff status, and expiration time. The expiration time is set to 1 hour from the current time. The payload is then encoded using the secret key and algorithm specified in the settings module.

    Example usage:
        user = User.objects.get(id=1)
        token = generate_token(user)
    """
    # Set the expiration time to 1 hour from now
    expiration_time = datetime.utcnow() + timedelta(
        hours=settings.TOKEN_EXPIRATION_TIME
    )
    payload = {
        "user_id": str(user.id),
        "exp": expiration_time,
    }
    secret_key = settings.SECRET_KEY  # Replace with your own secret key
    algorithm = settings.HASH_ALGORITHM  # Choose the desired algorithm, such as 'HS256'
    token = jwt.encode(payload, secret_key, algorithm)
    if not token:
        return {"message": "Error generating token", "status": 500}
    return token


def get_user_from_token(token):
    from managers.models import Managers

    # from customers.models import Customers

    """
    Decode a JWT token and retrieve the user associated with it.

    Parameters:
        - token (str): The JWT token to decode and retrieve the user from.

    Returns:
        - dict or None: If the token is valid and not expired, returns a dictionary containing the user information.
          If the token is invalid or expired, returns None.
    """
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.HASH_ALGORITHM]
        )
        user_id = payload.get("user_id")
        expiration_time = payload.get("exp")
        current_time = timezone.now().timestamp()
        if expiration_time is not None and current_time > expiration_time:
            return None
        user = (
            Managers.objects.filter(pk=user_id).first()
            # or Customers.objects.filter(pk=user_id).first()
        )
        return user
    except jwt.exceptions.ExpiredSignatureError:
        return None
    except jwt.DecodeError:
        return None
    except Managers.DoesNotExist:
        return None


def validate_token(token):
    from managers.models import Managers

    # from customers.models import Customers

    """
    Validate a token for password reset.

    Args:
        token (str): The token to be validated.

    Returns:
        tuple: A tuple containing the user object and a boolean indicating if the token is valid.
    """
    user = (
        Managers.objects.filter(password_reset_token=token).first()
        # or Customers.objects.filter(password_reset_token=token).first()
    )
    if not user:
        return None, False
    if timezone.now() > user.password_reset_token_created_at + timezone.timedelta(
        hours=24
    ):
        return None, False
    return user, True


def generate_profile_id():
    """Generate a string like 'asac2323'."""
    letters = random.choices(string.ascii_lowercase, k=4)
    digits = random.choices(string.digits, k=4)
    return "".join(letters + digits)


def create_random_password():
    """
    Generate a random password.

    Returns:
        str: The randomly generated password.
    """
    password = get_random_string(length=20)  # Generate a random string of length 20
    return password
