# Generated by Django 4.1.7 on 2023-04-13 09:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("testapp", "0229_refered_by_master_delete_insurance_payement_detail_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="bookedappointments",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="bookedappointments",
            name="location",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="testapp.locationmaster",
            ),
        ),
    ]
