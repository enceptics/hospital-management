# Generated by Django 4.0.1 on 2022-12-05 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0061_remove_doctoraccounting_bill_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctoraccounting',
            name='tariff_name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
