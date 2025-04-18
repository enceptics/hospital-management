# Generated by Django 4.1.7 on 2023-04-15 05:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("testapp", "0232_vitalsign_created_by_vitalsign_location_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="opdbillingmain",
            name="batch_no",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="opdbillingmain",
            name="paid_claim_amt",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="tokencreations",
            name="Date",
            field=models.DateField(default=datetime.date(2023, 4, 15)),
        ),
    ]
