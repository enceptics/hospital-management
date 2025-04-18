# Generated by Django 4.0.1 on 2023-03-10 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0158_refferal_notes_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseSummery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uhid', models.CharField(max_length=100)),
                ('patient_name', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('hosp_no', models.CharField(max_length=100)),
                ('tel_no', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('d_o_a', models.CharField(max_length=100)),
                ('d_o_d', models.CharField(max_length=100)),
                ('consultant', models.CharField(max_length=100)),
                ('dept', models.CharField(max_length=100)),
                ('medical_history', models.CharField(max_length=100)),
                ('physi_find', models.CharField(max_length=100)),
                ('investigation', models.CharField(max_length=100)),
                ('management', models.CharField(max_length=100)),
                ('treat_discharge', models.CharField(max_length=100)),
                ('recommendation', models.CharField(max_length=100)),
                ('follow_up', models.CharField(max_length=100)),
                ('day', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=100)),
                ('name_sign', models.CharField(max_length=100)),
                ('doctor_notes', models.CharField(max_length=100)),
            ],
        ),
    ]
