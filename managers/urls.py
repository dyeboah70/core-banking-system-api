from django.urls import path
from managers.api_views.signup import create_staff
from managers.api_views.login import LoginView
from managers.api_views.otp_verification import otp_verification_view
from managers.api_views.otp_resend import otp_code_resend_view
from managers.api_views.password_reset import password_reset_request_view
from managers.api_views.password_reset_confirmation import password_reset_confirm_view
from managers.api_views.staffs import list_staffs
from managers.api_views.staff_details import staff_details
from managers.api_views.roles import roles
from managers.api_views.token_verification import verify_token

app_name = "staffs"

urlpatterns = [
    path("signup/", create_staff, name="signup"),
    path("roles/", roles, name="roles"),
    path("verify-token/", verify_token, name="verify-token"),
    path("staffs/", list_staffs, name="staffs"),
    path("staff-details/", staff_details, name="staff-details"),
    path("password-reset/", password_reset_request_view, name="password-reset"),
    path(
        "password-reset/confirm/<slug:token>/",
        password_reset_confirm_view,
        name="password-reset-confirm",
    ),
    path("login/", LoginView.as_view(), name="login"),
    path("resend-otp/", otp_code_resend_view, name="resend-otp"),
    path("otp-verification/", otp_verification_view, name="otp-verification"),
]
