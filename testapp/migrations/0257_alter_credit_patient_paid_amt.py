# Generated by Django 4.1.7 on 2023-04-20 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("testapp", "0256_alter_department_consumption_consumption_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="credit",
            name="patient_paid_amt",
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
