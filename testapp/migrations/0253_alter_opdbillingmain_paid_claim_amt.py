# Generated by Django 4.1.7 on 2023-04-20 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("testapp", "0252_alter_opdbillingmain_paid_claim_amt"),
    ]

    operations = [
        migrations.AlterField(
            model_name="opdbillingmain",
            name="paid_claim_amt",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
