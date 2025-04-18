# Generated by Django 4.0.1 on 2022-11-25 09:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0049_alter_opdbillsettlementtemp_bill_amt_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='opdbillsettlementtemp',
            name='cheque_no',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='opdbillsettlementtemp',
            name='paymennt_mode',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='centralisedadminview',
            name='Date',
            field=models.DateField(default=datetime.date(2022, 11, 25)),
        ),
        migrations.AlterField(
            model_name='tokencreationdone',
            name='Date',
            field=models.DateField(default=datetime.date(2022, 11, 25)),
        ),
        migrations.AlterField(
            model_name='tokencreations',
            name='Date',
            field=models.DateField(default=datetime.date(2022, 11, 25)),
        ),
    ]
