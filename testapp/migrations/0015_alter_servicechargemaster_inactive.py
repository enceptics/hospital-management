# Generated by Django 4.0.1 on 2022-10-12 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0014_alter_servicechargemaster_inactive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicechargemaster',
            name='inactive',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
