# Generated by Django 4.0.1 on 2023-03-06 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0151_ins_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientvisitmains',
            name='nurse_doctor',
        ),
        migrations.AddField(
            model_name='patientvisitmains',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='testapp.doctortable'),
        ),
    ]
