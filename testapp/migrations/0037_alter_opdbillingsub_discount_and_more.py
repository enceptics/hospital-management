# Generated by Django 4.0.1 on 2022-11-14 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0036_remove_opdbillingmain_service_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opdbillingsub',
            name='discount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='opdbillingsub',
            name='outstanding_amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='opdbillingsub',
            name='paid_amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='opdbillingsub',
            name='pay_amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='opdbillingsub',
            name='payment_mode',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
