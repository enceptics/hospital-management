# Generated by Django 4.0.1 on 2023-03-31 15:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0183_alter_doctortable_doctor_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctortable',
            name='doctor_phone_no',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tokencreations',
            name='Date',
            field=models.DateField(default=datetime.date(2023, 3, 31)),
        ),
    ]
