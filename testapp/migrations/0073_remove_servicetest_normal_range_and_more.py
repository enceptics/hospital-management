# Generated by Django 4.0.1 on 2022-12-15 16:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0072_alter_profileservice_discount_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicetest',
            name='normal_range',
        ),
        migrations.AddField(
            model_name='servicetest',
            name='chield_range',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='servicetest',
            name='female_range',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='servicetest',
            name='infant_range',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='servicetest',
            name='male_range',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='centralisedadminview',
            name='Date',
            field=models.DateField(default=datetime.date(2022, 12, 15)),
        ),
        migrations.AlterField(
            model_name='tokencreationdone',
            name='Date',
            field=models.DateField(default=datetime.date(2022, 12, 15)),
        ),
        migrations.AlterField(
            model_name='tokencreations',
            name='Date',
            field=models.DateField(default=datetime.date(2022, 12, 15)),
        ),
    ]
