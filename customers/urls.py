from django.urls import path
from customers.api_views.user_setup import create_customer
from customers.api_views.customers import list_customers
from customers.api_views.customer_details import customer_details
from customers.api_views.profile_update import update_customer
from customers.api_views.approve_account import update_status

app_name = "customers"
urlpatterns = [
    path("create-customer/", create_customer, name="create-customer"),
    path("update-status/<slug:profile_id>/",
         update_status,
         name="update-status"),
    path("list-customers/", list_customers, name="list-customers"),
    path("customer-details/", customer_details, name="customer-details"),
    path('update-customer/<slug:profile_id>/',
         update_customer,
         name='update-customer'),
]
