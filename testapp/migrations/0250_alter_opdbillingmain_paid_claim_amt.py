# Generated by Django 4.1.7 on 2023-04-20 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("testapp", "0249_transfer_request_mainstore_parent_item_issue_no"),
    ]

    operations = [
        migrations.AlterField(
            model_name="opdbillingmain",
            name="paid_claim_amt",
            field=models.CharField(blank=True, default="0", max_length=50, null=True),
        ),
    ]
