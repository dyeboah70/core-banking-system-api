# Generated by Django 4.1.7 on 2023-10-25 14:36

import accounts.utils
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("customers", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AccountTypes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "account_type",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "maximum_withdrawal_amount",
                    models.DecimalField(decimal_places=2, max_digits=12),
                ),
                (
                    "annual_interest_rate",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="Interest rate from 0 - 100",
                        max_digits=5,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(100),
                        ],
                    ),
                ),
                (
                    "interest_calculation_per_year",
                    models.PositiveSmallIntegerField(
                        help_text="The number of times interest will be calculated per year",
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(12),
                        ],
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Accounts",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="customers.customers",
                    ),
                ),
                (
                    "account_number",
                    models.CharField(
                        blank=True,
                        default=accounts.utils.generate_account_number,
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "balance",
                    models.DecimalField(decimal_places=2, default=0, max_digits=12),
                ),
                (
                    "interest_start_date",
                    models.DateField(
                        blank=True,
                        help_text="The month number that interest calculation will start from",
                        null=True,
                    ),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("initial_deposit_date", models.DateField(blank=True, null=True)),
                (
                    "account_type",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="accounts",
                        to="accounts.accounttypes",
                    ),
                ),
            ],
        ),
    ]