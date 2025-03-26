# Generated by Django 4.1.7 on 2023-04-11 10:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("testapp", "0221_remove_createuser_store_createuser_store"),
    ]

    operations = [
        migrations.RenameField(
            model_name="tokencreations",
            old_name="Pt_Id",
            new_name="Patient_Id",
        ),
        migrations.RenameField(
            model_name="tokencreations",
            old_name="Pt_Name",
            new_name="Patient_Name",
        ),
        migrations.AddField(
            model_name="ps_countersale_parent",
            name="location_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="testapp.locationmaster",
            ),
        ),
        migrations.AddField(
            model_name="ps_countersale_parent",
            name="store_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="testapp.storemaster",
            ),
        ),
        migrations.AlterField(
            model_name="patientregistrationsub",
            name="alternate_contact_number",
            field=models.CharField(blank=True, default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="patientsregistrationsallinone",
            name="alternate_contact_number",
            field=models.CharField(blank=True, default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="tokencreations",
            name="Date",
            field=models.DateField(default=datetime.date(2023, 4, 11)),
        ),
    ]
