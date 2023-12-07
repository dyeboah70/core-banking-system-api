from django.db import models
from customers.models import Customers
import uuid


class Transactions(models.Model):
    user = models.ForeignKey(
        Customers, on_delete=models.CASCADE, related_name="transactions"
    )
    amount = models.FloatField()
    account_number = models.CharField(max_length=255, blank=True, null=True)
    teller_id = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateField(auto_now_add=True)
    transaction_id = models.UUIDField(default=uuid.uuid4, unique=True)
    reference_number = models.CharField(max_length=255, blank=True, null=True)
    transaction_type = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        choices=[("deposit", "deposit"), ("withdrawal", "withdrawal")],
        default="deposit",
    )

    def __str__(self):
        return self.user.first_name
