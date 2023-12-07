from django.test import TestCase

# Create your tests here.
from django.utils import timezone
from deposits.models import Deposits
from customers.models import Customers


def create_customers():
    return Customers.objects.create(
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


class DepositsModelTests(TestCase):
    def setUp(self):
        # Set up the necessary objects for the tests
        self.user = create_customers()
        self.deposit = Deposits.objects.create(
            user=self.user,
            amount=100.00,
            date_created=timezone.now(),
            narration="Test deposit",
            deposit_type="cash"
        )

    def test_deposit_creation(self):
        # Test that a deposit is created properly
        self.assertEqual(self.deposit.user, self.user)
        self.assertEqual(self.deposit.amount, 100.00)
        self.assertIsNotNone(self.deposit.date_created)
        self.assertEqual(self.deposit.narration, "Test deposit")
        self.assertEqual(self.deposit.deposit_type, "cash")

    def test_deposit_str_representation(self):
        # Test the string representation of the deposit
        self.assertEqual(str(self.deposit), self.user.first_name)
