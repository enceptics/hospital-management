# Generated by Django 4.0.1 on 2023-02-08 12:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0143_alter_centralisedadminview_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preventory_Maintanence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_sub_id', models.CharField(max_length=100)),
                ('item_model_no', models.CharField(max_length=100)),
                ('done_by', models.CharField(max_length=100)),
                ('done_date', models.CharField(max_length=100)),
                ('due_date', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('remark', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Unplanned_Maintanence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_sub_id', models.CharField(max_length=100)),
                ('item_model_no', models.CharField(max_length=100)),
                ('done_by', models.CharField(max_length=100)),
                ('problem_occure_date', models.CharField(max_length=100)),
                ('problem_name', models.CharField(max_length=30)),
                ('remark', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='centralisedadminview',
            name='Date',
            field=models.DateField(default=datetime.date(2023, 2, 8)),
        ),
        migrations.AlterField(
            model_name='tokencreationdone',
            name='Date',
            field=models.DateField(default=datetime.date(2023, 2, 8)),
        ),
        migrations.AlterField(
            model_name='tokencreations',
            name='Date',
            field=models.DateField(default=datetime.date(2023, 2, 8)),
        ),
    ]
