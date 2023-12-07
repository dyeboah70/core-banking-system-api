from django.contrib.auth.backends import ModelBackend
from managers.models import Managers


class AuthenticateManagers(ModelBackend):
    # Staff Authentication (email, password)
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = Managers.objects.get(email=email)
            if user.check_password(password):
                return user
        except Managers.DoesNotExist:
            return None
