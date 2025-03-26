# Generated by Django 4.0.1 on 2023-03-30 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0181_alter_patientsregistrationsallinone_nhif_ins_cor_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientsregistrationsallinone',
            name='sum_insured_amount',
            field=models.IntegerField(blank=True, default='0', null=True),
        ),
        migrations.AlterField(
            model_name='patientsregistrationsallinone',
            name='valid_upto',
            field=models.DateField(blank=True, null=True),
        ),
    ]
