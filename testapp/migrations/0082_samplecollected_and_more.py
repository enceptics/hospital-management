# Generated by Django 4.0.1 on 2022-12-16 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0081_rename_lab_service_id_saamplecollection_test_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='SampleCollected',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_id', models.CharField(max_length=100)),
                ('uhid', models.CharField(max_length=100)),
                ('visit_no', models.CharField(max_length=100)),
                ('bill_no', models.CharField(max_length=100)),
                ('profile_id', models.CharField(max_length=100)),
                ('profile_name', models.CharField(max_length=100)),
                ('date_time', models.DateTimeField()),
            ],
        ),
        migrations.RenameModel(
            old_name='SaampleCollection',
            new_name='SampleCollection',
        ),
    ]
