from django.test import TestCase
from withdrawals.models import Withdrawals
from customers.models import Customers


def create_customers(**kwargs):
    customer = Customers.objects.create(
        first_name="test",
        last_name="test",
        email="test@example.com",
        mobile_number="test",
        occupation="test",
        sex="MALE",
        **kwargs
    )
    kwargs.update({"customer": customer})
    return customer


class WithdrawalsTestCase(TestCase):
    def test_create_withdrawals(self):
        user = create_customers()
        withdrawals = Withdrawals.objects.create(
            user=user,
            amount=100,
            narration="test"
        )

        self.assertEqual(Withdrawals.objects.count(), 1)
        self.assertEqual(withdrawals.user, user)
