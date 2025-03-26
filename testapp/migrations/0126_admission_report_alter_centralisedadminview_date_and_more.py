# Generated by Django 4.0.1 on 2023-01-27 10:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0125_bookedappointments_admin_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admission_Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dr_name', models.CharField(blank=True, max_length=50)),
                ('uhid', models.CharField(blank=True, max_length=50)),
                ('admission_no', models.CharField(blank=True, max_length=50)),
                ('admission_date', models.CharField(blank=True, max_length=50)),
                ('first_name', models.CharField(blank=True, max_length=50)),
                ('mid_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('age', models.CharField(blank=True, max_length=50)),
                ('sex', models.CharField(blank=True, max_length=50)),
                ('doctor_name', models.CharField(blank=True, max_length=50)),
                ('department', models.CharField(blank=True, max_length=50)),
                ('sponsor', models.CharField(blank=True, max_length=50)),
                ('ward', models.CharField(blank=True, max_length=50)),
                ('bed_no', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='centralisedadminview',
            name='Date',
            field=models.DateField(default=datetime.date(2023, 1, 27)),
        ),
        migrations.AlterField(
            model_name='tokencreationdone',
            name='Date',
            field=models.DateField(default=datetime.date(2023, 1, 27)),
        ),
        migrations.AlterField(
            model_name='tokencreations',
            name='Date',
            field=models.DateField(default=datetime.date(2023, 1, 27)),
        ),
    ]
