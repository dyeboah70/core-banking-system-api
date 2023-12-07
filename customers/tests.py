from django.test import RequestFactory, TestCase
from django.test import TestCase,  RequestFactory
from customers.models import Customers
from customers.api_views.user_setup import create_customer
from unittest.mock import patch
from managers.models import Managers, Roles


class CustomersTestCase(TestCase):
    def test_create_customer(self):
        customer = Customers.objects.create(
            email="a@b.com",
            mobile_number="0777777777",
            occupation="Occupation",
            first_name="First Name",
            last_name="Last Name",
            ghana_card_number="123456789",
            date_of_birth="2000-01-01",
            city="City",
            postal_address="Postal Address",
            sex="MALE",
            marital_status="SINGLE",
            next_of_kin_name="Next of Kin Name",
            next_of_kin_phone_number="Next of Kin Phone Number",
            next_of_kin_address="Next of Kin Address",
            next_of_kin_relationship="Next of Kin Relationship",
        )

        self.assertEqual(customer.email, "a@b.com")
        self.assertEqual(customer.mobile_number, "0777777777")
        self.assertEqual(customer.occupation, "Occupation")
        self.assertEqual(customer.first_name, "First Name")
        self.assertEqual(customer.last_name, "Last Name")
        self.assertEqual(customer.ghana_card_number, "123456789")
        self.assertEqual(customer.date_of_birth, "2000-01-01")
        self.assertEqual(customer.city, "City")
        self.assertEqual(customer.postal_address, "Postal Address")
        self.assertEqual(customer.sex, "MALE")
        self.assertEqual(customer.marital_status, "SINGLE")
        self.assertEqual(customer.next_of_kin_name, "Next of Kin Name")
        self.assertEqual(customer.next_of_kin_phone_number,
                         "Next of Kin Phone Number")
        self.assertEqual(customer.next_of_kin_address, "Next of Kin Address")
        self.assertEqual(customer.next_of_kin_relationship,
                         "Next of Kin Relationship")


def create_managers():
    name = "IT_MANAGER"
    role = Roles.objects.create(name=name)
    managers = Managers.objects.create(
        email="a@b.com",
        first_name="First Name",
        last_name="Last Name",
        phone_number="0777777777",
        staff_id="123456789",
    )

    managers.roles.add(role)
    managers.save()
    return managers


class CreateCustomerTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = create_managers()

    @patch('customers.api_views.user_setup.check_permission')
    @patch('customers.api_views.user_setup.require_POST')
    def test_create_customer(self, mock_require_post, mock_check_permission):
        # Set up mock objects and data
        mock_require_post.return_value = lambda func: func
        mock_check_permission.return_value = lambda func: func

        request_data = {
            "email": "test@example.com",
            "mobile_number": "1234567890",
            "occupation": "Engineer",
            "first_name": "John",
            "last_name": "Doe",
            "ghana_card_number": "1234567890",
            "date_of_birth": "1990-01-01",
            "city": "New York",
            "postal_address": "123 Main St",
            "sex": "Male",
            "marital_status": "Single",
            "next_of_kin_name": "Jane Doe",
            "next_of_kin_phone_number": "0987654321",
            "next_of_kin_address": "456 Elm St",
            "next_of_kin_relationship": "Sibling",
            "account_type": 1,
        }

        # Use a mocked token
        headers = {'HTTP_AUTHORIZATION': 'Bearer MOCKED_TOKEN'}

        request = self.factory.post(
            '/customers:create-customer/', data=request_data, **headers)
        request.user = self.user

        # Call the view function
        response = create_customer(request)

        self.assertEqual(response.status_code, 403)
