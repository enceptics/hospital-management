# Generated by Django 4.0.1 on 2023-03-12 20:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0159_casesummery'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientAllergy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uhid', models.CharField(blank=True, max_length=50, null=True)),
                ('bill_id', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('visit_id', models.CharField(blank=True, max_length=100, null=True)),
                ('type', models.CharField(blank=True, choices=[('Drug', 'Drug'), ('Food', 'Food'), ('Insect', 'Insect'), ('Latex', 'Latex'), ('Mold', 'Mold')], max_length=100, null=True)),
                ('allergen', models.CharField(blank=True, choices=[('Drug', 'Drug'), ('Food', 'Food'), ('Insect', 'Insect'), ('Latex', 'Latex')], max_length=100, null=True)),
                ('reaction', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='centralisedadminview',
            name='Date',
            field=models.DateField(default=datetime.date(2023, 3, 12)),
        ),
        migrations.AlterField(
            model_name='tokencreationdone',
            name='Date',
            field=models.DateField(default=datetime.date(2023, 3, 12)),
        ),
        migrations.AlterField(
            model_name='tokencreations',
            name='Date',
            field=models.DateField(default=datetime.date(2023, 3, 12)),
        ),
    ]
