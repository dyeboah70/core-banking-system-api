# Generated by Django 4.1.7 on 2023-10-26 10:21

import customers.utils
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("customers", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customers",
            name="profile_id",
            field=models.CharField(
                blank=True,
                default=customers.utils.generate_profile_id,
                max_length=255,
                null=True,
            ),
        ),
    ]
