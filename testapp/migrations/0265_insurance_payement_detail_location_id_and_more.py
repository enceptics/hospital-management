# Generated by Django 4.1.3 on 2023-04-27 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0264_makeitem_return_tocpc_temp_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='insurance_payement_detail',
            name='location_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='insurance_payement_detail',
            name='pay_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='insurance_payement_detail',
            name='receipt_no',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='insurance_payement_detail',
            name='user_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
