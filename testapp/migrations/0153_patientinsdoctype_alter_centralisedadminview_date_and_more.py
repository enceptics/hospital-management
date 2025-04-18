# Generated by Django 4.0.1 on 2023-03-07 12:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0152_remove_patientvisitmains_nurse_doctor_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientInsDocType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uhid', models.CharField(max_length=100)),
                ('doc_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='centralisedadminview',
            name='Date',
            field=models.DateField(default=datetime.date(2023, 3, 7)),
        ),
        migrations.AlterField(
            model_name='tokencreationdone',
            name='Date',
            field=models.DateField(default=datetime.date(2023, 3, 7)),
        ),
        migrations.AlterField(
            model_name='tokencreations',
            name='Date',
            field=models.DateField(default=datetime.date(2023, 3, 7)),
        ),
    ]
