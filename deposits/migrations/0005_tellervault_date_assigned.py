# Generated by Django 4.2.7 on 2023-11-20 09:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("deposits", "0004_tellervault"),
    ]

    operations = [
        migrations.AddField(
            model_name="tellervault",
            name="date_assigned",
            field=models.DateField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
