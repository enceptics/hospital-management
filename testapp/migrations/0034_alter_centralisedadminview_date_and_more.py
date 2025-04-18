# Generated by Django 4.0.1 on 2022-11-11 09:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0033_opdpayment_uhid_alter_centralisedadminview_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='centralisedadminview',
            name='Date',
            field=models.DateField(default=datetime.date(2022, 11, 11)),
        ),
        migrations.AlterField(
            model_name='opdpayment',
            name='bill_id',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='tokencreationdone',
            name='Date',
            field=models.DateField(default=datetime.date(2022, 11, 11)),
        ),
        migrations.AlterField(
            model_name='tokencreations',
            name='Date',
            field=models.DateField(default=datetime.date(2022, 11, 11)),
        ),
    ]
