# Generated by Django 4.0.1 on 2022-11-08 13:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0029_opdbillingmain_payment_mode'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adv_Visit_Creation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uhid', models.CharField(max_length=50)),
                ('advance_pay', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='centralisedadminview',
            name='Date',
            field=models.DateField(default=datetime.date(2022, 11, 8)),
        ),
        migrations.AlterField(
            model_name='tokencreationdone',
            name='Date',
            field=models.DateField(default=datetime.date(2022, 11, 8)),
        ),
        migrations.AlterField(
            model_name='tokencreations',
            name='Date',
            field=models.DateField(default=datetime.date(2022, 11, 8)),
        ),
    ]
