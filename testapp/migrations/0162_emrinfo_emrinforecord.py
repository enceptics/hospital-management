# Generated by Django 4.0.1 on 2023-03-12 22:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0161_triageinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmrInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uhid', models.CharField(blank=True, max_length=50, null=True)),
                ('bill_id', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('visit_id', models.CharField(blank=True, max_length=100, null=True)),
                ('visit_date', models.DateTimeField(blank=True, null=True)),
                ('patient_name', models.CharField(blank=True, max_length=100, null=True)),
                ('age', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(blank=True, max_length=100, null=True)),
                ('record_type', models.CharField(blank=True, choices=[('OPD', 'OPD'), ('IPD', 'IPD')], max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmrInfoRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medical_record_type', models.CharField(blank=True, choices=[('nurse_notes', 'nurse_notes'), ('doctor_prescription', 'doctor_prescription'), ('lab_report', 'lab_report'), ('patient_history', 'patient_history'), ('clinical_notes', 'clinical_notes'), ('consultant_notes', 'consultant_notes'), ('consultant_order', 'consultant_order'), ('medical_details', 'medical_details')], max_length=100, null=True)),
                ('medical_record_file', models.FileField(null=True, upload_to='medical_record/')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('emrinfo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='emrinfo_record', to='testapp.emrinfo')),
            ],
        ),
    ]
