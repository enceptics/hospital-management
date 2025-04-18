# Generated by Django 4.0.1 on 2022-05-19 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0004_alter_centralisedadminview_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpdBillingTemp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_no', models.CharField(max_length=50)),
                ('bill_id', models.CharField(max_length=50)),
                ('bill_date_time', models.DateTimeField(auto_now_add=True)),
                ('uhid', models.CharField(max_length=50)),
                ('visit_no', models.CharField(max_length=50)),
                ('service_name', models.CharField(max_length=50)),
                ('rate', models.FloatField()),
                ('discount', models.IntegerField()),
                ('unit', models.IntegerField()),
                ('net_ammount', models.FloatField()),
                ('outstanding_amount', models.FloatField()),
                ('total_amount', models.FloatField()),
                ('receive_amount', models.FloatField()),
            ],
        ),
    ]
