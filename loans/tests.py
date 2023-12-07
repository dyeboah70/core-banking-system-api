from django.test import TestCase
from django.utils import timezone
from loans.models import LoanType, Loan, Repayment
from customers.models import Customers


class LoanTypeModelTests(TestCase):
    def setUp(self):
        # Set up the necessary objects for the tests
        self.loan_type = LoanType.objects.create(
            name="Personal Loan",
            annual_interest_rate=5.0,
            interest_calculation_per_year=12
        )

    def test_loan_type_creation(self):
        # Test that a loan type is created properly
        self.assertEqual(self.loan_type.name, "Personal Loan")
        self.assertEqual(self.loan_type.annual_interest_rate, 5.0)
        self.assertEqual(self.loan_type.interest_calculation_per_year, 12)

    def test_loan_type_str_representation(self):
        # Test the string representation of the loan type
        self.assertEqual(str(self.loan_type), "Personal Loan")


class LoanModelTests(TestCase):
    def setUp(self):
        # Set up the necessary objects for the tests
        self.user = Customers.objects.create(
            first_name="John",
            last_name="Doe",
            email="johndoe@example.com",
            mobile_number="1234567890"
        )
        self.loan_type = LoanType.objects.create(
            name="Personal Loan",
            annual_interest_rate=5.0,
            interest_calculation_per_year=12
        )
        self.loan = Loan.objects.create(
            borrower=self.user,
            amount=1000.00,
            date_applied=timezone.now(),
            interest_amount=100.00,
            amount_to_pay=1100.00,
            approved=True,
            interest_start_date=timezone.now().date(),
            loan_type=self.loan_type
        )

    def test_loan_creation(self):
        # Test that a loan is created properly
        self.assertEqual(self.loan.borrower, self.user)
        self.assertEqual(self.loan.amount, 1000.00)
        self.assertIsNotNone(self.loan.date_applied)
        self.assertEqual(self.loan.interest_amount, 100.00)
        self.assertEqual(self.loan.amount_to_pay, 1100.00)
        self.assertTrue(self.loan.approved)
        self.assertIsNotNone(self.loan.interest_start_date)
        self.assertEqual(self.loan.loan_type, self.loan_type)

    def test_loan_str_representation(self):
        # Test the string representation of the loan
        expected_str = f"{self.user} - 1000.0 - {self.loan.date_applied}"
        self.assertEqual(str(self.loan), expected_str)


class RepaymentModelTests(TestCase):
    def setUp(self):
        # Set up the necessary objects for the tests
        self.user = Customers.objects.create(
            first_name="John",
            last_name="Doe",
            email="johndoe@example.com",
            mobile_number="1234567890"
        )
        self.loan_type = LoanType.objects.create(
            name="Personal Loan",
            annual_interest_rate=5.0,
            interest_calculation_per_year=12
        )
        self.loan = Loan.objects.create(
            borrower=self.user,
            amount=1000.00,
            date_applied=timezone.now(),
            interest_amount=100.00,
            amount_to_pay=1100.00,
            approved=True,
            interest_start_date=timezone.now().date(),
            loan_type=self.loan_type
        )
        self.repayment = Repayment.objects.create(
            loan=self.loan,
            amount=100.00,
            due_date=timezone.now().date(),
            installment_number=1,
            teller_id="T123456"
        )

    def test_repayment_creation(self):
        # Test that a repayment is created properly
        self.assertEqual(self.repayment.loan, self.loan)
        self.assertEqual(self.repayment.amount, 100.00)
        self.assertIsNotNone(self.repayment.due_date)
        self.assertEqual(self.repayment.installment_number, 1)
        self.assertEqual(self.repayment.teller_id, "T123456")

    def test_repayment_str_representation(self):
        # Test the string representation of the repayment
        expected_str = f"{self.loan} - 100.0 - {self.repayment.due_date}"
        self.assertEqual(str(self.repayment), expected_str)
