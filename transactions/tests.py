from django.test import TestCase
from django.utils import timezone
from transactions.models import Transactions
from customers.models import Customers


class TransactionsModelTests(TestCase):
    def setUp(self):
        # Set up the necessary objects for the tests
        self.user = Customers.objects.create(
            first_name="John",
            last_name="Doe",
            email="johndoe@example.com",
            mobile_number="1234567890"
        )
        self.transaction = Transactions.objects.create(
            user=self.user,
            amount=100.00,
            account_number="123456789",
            teller_id="T123456",
            date_created=timezone.now().date(),
            reference_number="REF123",
            transaction_type="deposit"
        )

    def test_transaction_creation(self):
        # Test that a transaction is created properly
        self.assertEqual(self.transaction.user, self.user)
        self.assertEqual(self.transaction.amount, 100.00)
        self.assertEqual(self.transaction.account_number, "123456789")
        self.assertEqual(self.transaction.teller_id, "T123456")
        self.assertIsNotNone(self.transaction.date_created)
        self.assertEqual(self.transaction.reference_number, "REF123")
        self.assertEqual(self.transaction.transaction_type, "deposit")

    def test_transaction_str_representation(self):
        # Test the string representation of the transaction
        self.assertEqual(str(self.transaction), self.user.first_name)
