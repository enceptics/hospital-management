# Generated by Django 4.0.1 on 2022-11-23 14:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0041_credit_bill_date_time_credit_bill_no_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OPDBillSettlement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uhid', models.CharField(max_length=50)),
                ('visit_id', models.CharField(max_length=50)),
                ('bill_no', models.CharField(max_length=50)),
                ('bill_date', models.CharField(max_length=50)),
                ('bill_amt', models.CharField(max_length=50)),
                ('net_payable_amt', models.FloatField()),
                ('paid_amt', models.FloatField()),
                ('payment_amt', models.FloatField()),
                ('payment_mode', models.CharField(max_length=50)),
                ('status', models.BooleanField(choices=[('active', 'active'), ('inactive', 'inactive')])),
            ],
        ),
        migrations.AlterField(
            model_name='centralisedadminview',
            name='Date',
            field=models.DateField(default=datetime.date(2022, 11, 23)),
        ),
        migrations.AlterField(
            model_name='tokencreationdone',
            name='Date',
            field=models.DateField(default=datetime.date(2022, 11, 23)),
        ),
        migrations.AlterField(
            model_name='tokencreations',
            name='Date',
            field=models.DateField(default=datetime.date(2022, 11, 23)),
        ),
    ]
