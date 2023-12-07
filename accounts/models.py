from django.db import models
from decimal import Decimal
from customers.models import Customers
from accounts.utils import generate_account_number
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
)


class Accounts(models.Model):
    user = models.ForeignKey(
        Customers, on_delete=models.CASCADE)
    account_number = models.CharField(
        max_length=255, default=generate_account_number, blank=True, null=True
    )
    balance = models.DecimalField(
        default=0,
        max_digits=12,
        decimal_places=2
    )
    interest_start_date = models.DateField(
        null=True, blank=True,
        help_text=(
            'The month number that interest calculation will start from'
        )
    )
    date_created = models.DateTimeField(auto_now_add=True)
    account_type = models.ForeignKey(
        "AccountTypes", on_delete=models.CASCADE, blank=True, null=True, related_name='accounts',
    )
    initial_deposit_date = models.DateField(null=True, blank=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name

    def get_interest_calculation_months(self):
        """
        List of month numbers for which the interest will be calculated

        returns [2, 4, 6, 8, 10, 12] for every 2 months interval
        """
        interval = int(
            12 / self.account_type.interest_calculation_per_year
        )
        start = self.interest_start_date.month
        return [i for i in range(start, 13, interval)]


class AccountTypes(models.Model):
    account_type = models.CharField(max_length=255, blank=True, null=True)
    maximum_withdrawal_amount = models.DecimalField(
        decimal_places=2,
        max_digits=12
    )
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
        return self.account_type

    def calculate_interest(self, principal):
        """
        Calculate interest for each account type.

        This uses a basic interest calculation formula
        """
        p = principal
        r = self.annual_interest_rate
        n = Decimal(self.interest_calculation_per_year)

        # Basic Future Value formula to calculate interest
        interest = (p * (1 + ((r/100) / n))) - p

        return round(interest, 2)
