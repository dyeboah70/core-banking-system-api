from django.db import models
from customers.models import Customers
from managers.models import Managers
import uuid


class Deposits(models.Model):
    user = models.ForeignKey(
        Customers, on_delete=models.CASCADE, related_name="deposits"
    )
    amount = models.DecimalField(
        default=0.0, blank=True, null=True, decimal_places=2, max_digits=12
    )
    date_created = models.DateTimeField(auto_now_add=True)
    narration = models.CharField(max_length=255, blank=True, null=True)
    deposit_id = models.UUIDField(default=uuid.uuid4, unique=True)
    deposit_type = models.ForeignKey(
        "DepositType",
        on_delete=models.CASCADE,
        related_name="deposits",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.user.first_name


class DepositType(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Vault(models.Model):
    amount = models.DecimalField(
        default=0.0, blank=True, null=True, decimal_places=2, max_digits=12
    )
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.amount}"


class TellerVault(models.Model):
    amount = models.DecimalField(default=0.0, decimal_places=2, max_digits=12)

    teller = models.ForeignKey(
        Managers, on_delete=models.CASCADE, related_name="teller_vault"
    )
    date_assigned = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.teller.first_name} {self.teller.last_name} {self.amount}"

    
    @property
    def get_full_name(self):
        return f"{self.teller.first_name} {self.teller.last_name}"
