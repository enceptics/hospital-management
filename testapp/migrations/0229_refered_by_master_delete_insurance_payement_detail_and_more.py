# Generated by Django 4.1.7 on 2023-04-13 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("testapp", "0228_insurance_payement_detail_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Refered_by_Master",
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
                ("Staff_name", models.CharField(max_length=100)),
                ("description", models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name="Insurance_Payement_Detail",
        ),
        migrations.RemoveField(
            model_name="opdbillingmain",
            name="paid_claim_amt",
        ),
    ]
