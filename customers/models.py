from django.db import models
from customers.utils import generate_profile_id
import os
import uuid


def user_image_file_path(instance, filename):
    """Generate file path for new recipe image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/customers', filename)


class Customers(models.Model):
    class MaritalStatus(models.TextChoices):
        SINGLE = "SINGLE"
        MARRIED = "MARRIED"

    class Sex(models.TextChoices):
        MALE = "MALE"
        FEMALE = "FEMALE"

    class Status(models.TextChoices):
        APPROVED = "APPROVED"
        PENDING = "PENDING"
        SUSPENDED = "SUSPENDED"
        DEACTIVATED = "DEACTIVATED"

    profile_id = models.CharField(max_length=255,
                                  default=generate_profile_id,
                                  blank=True,
                                  null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    ghana_card_number = models.CharField(max_length=255,
                                         blank=True,
                                         null=True,
                                         unique=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    mobile_number = models.CharField(max_length=255, blank=True, null=True)
    occupation = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    postal_address = models.CharField(max_length=255, blank=True, null=True)
    marital_status = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        choices=MaritalStatus.choices,
        default=MaritalStatus.SINGLE,
    )
    sex = models.CharField(max_length=255,
                           blank=True,
                           null=True,
                           choices=Sex.choices,
                           default=Sex.MALE)

    # Next of kin
    next_of_kin_name = models.CharField(max_length=255, blank=True, null=True)
    next_of_kin_phone_number = models.CharField(max_length=255,
                                                blank=True,
                                                null=True)
    next_of_kin_address = models.CharField(max_length=255,
                                           blank=True,
                                           null=True)
    next_of_kin_relationship = models.CharField(max_length=255,
                                                blank=True,
                                                null=True)

    is_approved = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        choices=Status.choices,
        default=Status.PENDING,
    )
    image = models.ImageField(null=True, upload_to=user_image_file_path)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
