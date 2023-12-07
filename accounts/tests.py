
from django.test import TestCase
from django.utils import timezone
from accounts.models import Accounts, AccountTypes
from customers.models import Customers


# helper function to create customers

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


def create_account_types():
    return AccountTypes.objects.create(
        account_type='Savings', maximum_withdrawal_amount=100.00, annual_interest_rate=5.00, interest_calculation_per_year=12)


class AccountsModelTests(TestCase):
    def setUp(self):
        # Set up the necessary objects for the tests
        self.user = create_customers()
        self.account_type = create_account_types()
        self.account = Accounts.objects.create(
            user=self.user,
            account_number='123456789',
            balance=100.00,
            interest_start_date=timezone.now().date(),
            account_type=self.account_type,
            initial_deposit_date=timezone.now().date()
        )

    def test_account_creation(self):
        # Test that an account is created properly
        self.assertEqual(self.account.user, self.user)
        self.assertEqual(self.account.account_number, '123456789')
        self.assertEqual(self.account.balance, 100.00)
        self.assertEqual(
            self.account.interest_start_date,
            timezone.now().date()
        )
        self.assertEqual(self.account.account_type, self.account_type)
        self.assertEqual(
            self.account.initial_deposit_date,
            timezone.now().date()
        )

    def test_invalid_account_creation(self):
        # Test that an account is created properly
        with self.assertRaises(Exception):
            Accounts.objects.create(
                user=self.user,
                account_number='123456789',
                balance=100.00,
                interest_start_date=timezone.now().date(),
                account_type=self.account_type,
                initial_deposit_date=timezone.now().date()
            )

    def test_interest_calculation_months(self):
        # Test that the interest calculation months are correct
        self.assertEqual(
            self.account.get_interest_calculation_months(),
            [10, 11, 12]
        )
