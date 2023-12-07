from django.db import models
from datetime import datetime, timedelta
from customers.models import Customers
from decimal import Decimal
from django.core.validators import MinValueValidator
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
)


class LoanType(models.Model):
    name = models.CharField(max_length=128)
    annual_interest_rate = models.DecimalField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        decimal_places=2,
        max_digits=5,
        help_text='Interest rate from 0 - 100'
    )
    interest_calculation_per_year = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(12)],
        help_text='The number of times interest will be calculated per year'
    )

    def __str__(self):
        return self.name


class Loan(models.Model):
    borrower = models.ForeignKey(Customers, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_applied = models.DateTimeField(auto_now_add=True)
    interest_amount = models.DecimalField(max_digits=10,
                                          decimal_places=2,
                                          default=0.0)

    amount_to_pay = models.DecimalField(max_digits=10,
                                        decimal_places=2,
                                        blank=True,
                                        null=True)
    approved = models.BooleanField(default=False)
    interest_start_date = models.DateField(
        null=True, blank=True,
        help_text=(
            'The month number that interest calculation will start from'
        )
    )
    loan_type = models.ForeignKey(LoanType, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.borrower} - {self.amount} - {self.date_applied}"

    def calculate_interest(self, principal):
        """
        Calculate interest for each account type.

        This uses a basic interest calculation formula
        """
        p = principal
        r = self.loan_type.annual_interest_rate
        n = Decimal(self.loan_type.interest_calculation_per_year)

        # Basic Future Value formula to calculate interest
        interest = (p * (1 + ((r/100) / n))) - p

        return round(interest, 2)

    def get_interest_calculation_months(self):
        """
        List of month numbers for which the interest will be calculated

        returns [2, 4, 6, 8, 10, 12] for every 2 months interval
        """
        interval = int(
            12 / self.loan_type_type.interest_calculation_per_year
        )
        start = self.interest_start_date.month
        return [i for i in range(start, 13, interval)]


class Repayment(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField(auto_now_add=True)
    installment_number = models.PositiveIntegerField(
        validators=[MinValueValidator(1)], blank=True, null=True)
    teller_id = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.loan} - {self.amount} - {self.due_date}"
