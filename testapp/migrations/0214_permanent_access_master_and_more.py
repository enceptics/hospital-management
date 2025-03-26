# Generated by Django 4.1.2 on 2023-04-08 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0213_remove_inventory_itemmaster_gst_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permanent_Access_Master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='addmembers',
            name='patient_name',
        ),
        migrations.RemoveField(
            model_name='bookedappointments',
            name='patient_name',
        ),
        migrations.RemoveField(
            model_name='newappointmentbyadmin',
            name='patient_name',
        ),
        migrations.AddField(
            model_name='addmembers',
            name='first_name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='addmembers',
            name='last_name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='addmembers',
            name='middle_name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='bookedappointments',
            name='first_name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookedappointments',
            name='last_name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='bookedappointments',
            name='middle_name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='newappointmentbyadmin',
            name='first_name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newappointmentbyadmin',
            name='last_name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='newappointmentbyadmin',
            name='middle_name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='bookedappointments',
            name='patient_gender',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='bookedappointments',
            name='patient_mobile_number',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='patientbillinginfos',
            name='relation',
            field=models.CharField(blank=True, default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patientbillinginfos',
            name='sum_insured_amount',
            field=models.CharField(blank=True, default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patientsregistrationsallinone',
            name='ins_doc_upload',
            field=models.ImageField(blank=True, default=1, upload_to='ins_document/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patientsregistrationsallinone',
            name='ins_id_upload',
            field=models.ImageField(blank=True, default=1, upload_to='ins_id_document/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patientsregistrationsallinone',
            name='nhif_ins_cor_name',
            field=models.CharField(blank=True, default='Cash', max_length=100),
        ),
        migrations.AlterField(
            model_name='patientsregistrationsallinone',
            name='relation',
            field=models.CharField(blank=True, default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patientsregistrationsallinone',
            name='sum_insured_amount',
            field=models.CharField(blank=True, default='0', max_length=100),
        ),
    ]
