from django.db import models
from .common import ManagersCommonFields
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager


class Managers(ManagersCommonFields, AbstractBaseUser, PermissionsMixin):
    # Models for TELLER, MANAGER, IT_MANAGER
    email = models.EmailField(unique=True)
    roles = models.ManyToManyField("Roles",
                                   blank=True,
                                   related_name="managers")

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Roles(models.Model):
    name = models.CharField(max_length=20,
                            unique=True,
                            null=False,
                            blank=False)

    permissions = models.ManyToManyField("Permission",
                                         blank=True,
                                         related_name="roles")

    def __str__(self):
        return self.name


class Permission(models.Model):
    name = models.CharField(max_length=100,
                            unique=True,
                            null=False,
                            blank=False)
    allowed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
