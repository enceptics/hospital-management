# Generated by Django 4.0.1 on 2023-01-03 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0116_opdbillingsub_package_profile_amt_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='opdbillingtemper',
            name='package_profile_amt',
            field=models.CharField(blank=True, default='None', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='opdbillingtemper',
            name='package_profile_id',
            field=models.CharField(blank=True, default='None', max_length=50, null=True),
        ),
    ]
