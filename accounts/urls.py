from django.urls import path
from accounts.api_views.account import list_accounts
from accounts.api_views.account_type import account_types
from accounts.api_views.create_account_type import create_account_type
from accounts.api_views.update_account_type import update_account_type
from accounts.api_views.verify_account import verify_account_number
from accounts.api_views.assign_account import assign_account_to_customer
from accounts.api_views.account_details_by_card import get_account_data

app_name = "accounts"
urlpatterns = [
    path("accounts/", list_accounts, name="accounts"),
    path("account-types/", account_types, name="account-types"),
    path(
        "update-account-type/<int:account_type_id>/",
        update_account_type,
        name="update-account-type",
    ),
    path("create-account-type/", create_account_type, name="create-account-type"),
    path("verify-account-number/", verify_account_number, name="verify-account-number"),
    path(
        "assign-account-to-customer/",
        assign_account_to_customer,
        name="assign-account-to-customer",
    ),
    path("linked-accounts/", get_account_data, name="linked-accounts")
]
