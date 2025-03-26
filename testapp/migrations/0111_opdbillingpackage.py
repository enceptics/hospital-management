# Generated by Django 4.0.1 on 2023-01-02 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0110_opdbillingtemper_package_profile_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OPDBillingPackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uhid', models.CharField(max_length=100)),
                ('visit_no', models.CharField(max_length=100)),
                ('bill_no', models.CharField(max_length=100)),
                ('package_id', models.CharField(max_length=100)),
                ('package_name', models.CharField(max_length=100)),
                ('date_time', models.DateTimeField()),
            ],
        ),
    ]
