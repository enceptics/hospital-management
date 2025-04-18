# Generated by Django 4.0.1 on 2023-02-03 11:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0133_access_site_anticoagulation_asset_type_bruit_thrill_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estimate_bill_main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uhid', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('age', models.CharField(max_length=30)),
                ('sex', models.CharField(max_length=30)),
                ('contact_no', models.CharField(max_length=30)),
                ('services', models.CharField(max_length=300)),
                ('services_rate', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Estimate_bill_sub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uhid', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('age', models.CharField(max_length=30)),
                ('sex', models.CharField(max_length=30)),
                ('contact_no', models.CharField(max_length=30)),
                ('services', models.CharField(max_length=300)),
                ('services_rate', models.CharField(max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='centralisedadminview',
            name='Date',
            field=models.DateField(default=datetime.date(2023, 2, 3)),
        ),
        migrations.AlterField(
            model_name='tokencreationdone',
            name='Date',
            field=models.DateField(default=datetime.date(2023, 2, 3)),
        ),
        migrations.AlterField(
            model_name='tokencreations',
            name='Date',
            field=models.DateField(default=datetime.date(2023, 2, 3)),
        ),
    ]
