# Generated by Django 4.0.1 on 2022-10-28 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0023_remove_opdbillingtemper_bill_date_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='opdbillingmain',
            name='billing_group_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='opdbillingmain',
            name='corporate_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
