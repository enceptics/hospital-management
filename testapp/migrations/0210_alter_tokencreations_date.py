# Generated by Django 4.1.2 on 2023-04-07 10:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0209_prescriptiondialysis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tokencreations',
            name='Date',
            field=models.DateField(default=datetime.date(2023, 4, 7)),
        ),
    ]
