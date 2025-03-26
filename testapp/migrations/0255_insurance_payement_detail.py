# Generated by Django 4.1.7 on 2023-04-20 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("testapp", "0254_alter_opdbillingmain_paid_claim_amt"),
    ]

    operations = [
        migrations.CreateModel(
            name="Insurance_Payement_Detail",
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
                ("uhid", models.CharField(blank=True, max_length=50, null=True)),
                ("bill_id", models.CharField(max_length=50)),
                ("mode_type", models.CharField(max_length=30)),
                ("net_amount", models.FloatField(blank=True, null=True)),
                ("paid_amount", models.FloatField(blank=True, null=True)),
                ("pending_amount", models.FloatField(blank=True, null=True)),
                ("bank_no", models.CharField(blank=True, max_length=100, null=True)),
                ("card_no", models.CharField(blank=True, max_length=100, null=True)),
                ("paid_by", models.CharField(blank=True, max_length=100, null=True)),
                ("ref_number", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "mobile_nummber",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "card_holder_name",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("date_time", models.DateTimeField(auto_now_add=True, null=True)),
                ("status", models.CharField(max_length=100)),
            ],
        ),
    ]
