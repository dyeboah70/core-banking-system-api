from functools import wraps
from managers.models import Roles
from django.http import JsonResponse
from managers.utils import get_user_from_token
from django.core.exceptions import ValidationError
from my_package.config.json_reader import read_config
import os

SETTINGS_FILE = os.path.join("config/settings.json")
ALL_SETTINGS = read_config(SETTINGS_FILE)


def check_permission(required_permission):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            token = request.headers.get("Authorization", "").split(" ")[-1]

            if not token:
                response_data = {
                    "message": "Authorization header not provided.",
                    "status": 400,
                }
                return JsonResponse(response_data, status=400)

            rbac_data = None  # Initialize rbac_data with a default value

            try:
                user = get_user_from_token(token)
                if isinstance(user, dict):
                    return JsonResponse(user, status=401)
                # Load RBAC data from the database and store it in cache
                rbac_data = load_rbac_data_from_database()
            except ValidationError:
                response_data = {
                    "message": "Invalid token",
                    "status": 401,
                }
                return JsonResponse(response_data, status=401)

            if not has_permission(user, required_permission, rbac_data):
                response_data = {
                    "message": "You don't have permission to access this page.",
                    "status": 403,
                }
                return JsonResponse(response_data, status=403)

            return view_func(request, *args, **kwargs)

        return _wrapped_view

    return decorator


def load_rbac_data_from_database():
    roles = Roles.objects.all()
    rbac_data = ALL_SETTINGS["rbac_data"]

    for role in roles:
        perm_data = {}

        for permission in role.permissions.all():
            perm_data[permission.name] = {"allowed": permission.allowed}

        rbac_data[role.name] = {"perms": perm_data}

    return rbac_data


# def has_permission(user, required_permission, rbac_data):
#     user_roles = set(user.roles.values_list('name', flat=True))

#     for role, role_data in rbac_data.get('roles', {}).items():
#         perms = role_data.get('perms', {})
#         permission = perms.get(required_permission, {})

#         if role in user_roles:
#             if permission.get('allowed', False):
#                 return True

#     return False


def has_permission(user, required_permission, rbac_data):
    if user is not None and user.roles is not None:
        user_roles = set(user.roles.values_list("name", flat=True))
        print(user_roles)
    else:
        user_roles = set()

    for role, role_data in rbac_data.get("roles", {}).items():
        perms = role_data.get("perms", {})
        permission = perms.get(required_permission, {})

        if role in user_roles:
            if permission.get("allowed", False):
                return True

    return False
