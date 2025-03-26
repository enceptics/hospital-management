# Generated by Django 4.0.1 on 2023-02-03 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0136_estimate_bill_temp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estimate_bill_mains',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uhid', models.CharField(blank=True, max_length=30, null=True)),
                ('name', models.CharField(max_length=30)),
                ('age', models.CharField(max_length=30)),
                ('sex', models.CharField(max_length=30)),
                ('contact_no', models.CharField(max_length=30)),
                ('services', models.CharField(max_length=300)),
                ('services_rate', models.CharField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
