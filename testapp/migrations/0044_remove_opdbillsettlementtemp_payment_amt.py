# Generated by Django 4.0.1 on 2022-11-24 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0043_opdbillsettlementtemp_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opdbillsettlementtemp',
            name='payment_amt',
        ),
    ]
