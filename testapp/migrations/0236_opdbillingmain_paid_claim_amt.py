# Generated by Django 4.1.7 on 2023-04-15 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("testapp", "0235_remove_opdbillingmain_paid_claim_amt"),
    ]

    operations = [
        migrations.AddField(
            model_name="opdbillingmain",
            name="paid_claim_amt",
            field=models.CharField(blank=True, default="0", max_length=50, null=True),
        ),
    ]
