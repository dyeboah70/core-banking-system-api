from django.db import models
from customers.models import Customers


class Withdrawals(models.Model):
    user = models.ForeignKey(
        Customers, on_delete=models.CASCADE, related_name="withdrawals"
    )
    amount = models.DecimalField(
        default=0.0, blank=True, null=True, decimal_places=2, max_digits=12)
    date_created = models.DateTimeField(auto_now_add=True)
    narration = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.first_name
