from django.urls import path
from loans.api_views.create_loan import create_loan
from loans.api_views.list_loan import list_loans
from loans.api_views.loan_details import loan_details
from loans.api_views.approve_loan import approve_loan
from loans.api_views.has_finished_payment import has_user_finished_paying_loan
from loans.api_views.loan_repayment import loan_repayment
from loans.api_views.list_loan_types import list_loan_types
from loans.api_views.create_loan_types import create_loan_type
from loans.api_views.update_loan_type import update_loan_type

app_name = "loans"

urlpatterns = [
    path("create-loan/", create_loan, name="create-loan"),
    path("loan-repayment/", loan_repayment, name="loan-repayment"),
    path("list-loans/", list_loans, name="list-loans"),
    path("list-loan-types/", list_loan_types, name="list-loan-types"),
    path("update-loan-type/<int:loan_type_id>/",
         update_loan_type, name="update-loan-type"),
    path("create-loan-type/", create_loan_type, name="create-loan-type"),
    path("loan-details/", loan_details, name="loan-details"),
    path("approve-loan/<int:id>/", approve_loan, name="approve-loan"),
    path("has-finished-payment/<int:id>/",
         has_user_finished_paying_loan,
         name="has-finished-payment"),
]
