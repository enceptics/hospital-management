# Generated by Django 4.0.1 on 2023-01-30 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0128_post_dialysis_details_bp_standing_min_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pre_Dialysis_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uhid', models.CharField(max_length=30)),
                ('pre_post_dialysis', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('pre_equip_preparation', models.CharField(max_length=100)),
                ('physian', models.CharField(max_length=100)),
                ('primary_dialysis_theraphy', models.CharField(max_length=100)),
                ('secondry_dialysis_theraphy', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('cannulation_nurse', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('machine_name', models.CharField(max_length=100)),
                ('asset_type', models.CharField(max_length=100)),
                ('bruit_thrill', models.CharField(max_length=100)),
                ('cannulation_name', models.CharField(max_length=100)),
                ('access_site', models.CharField(max_length=100)),
                ('access_site_infection', models.CharField(max_length=100)),
                ('iso_uf', models.CharField(max_length=100)),
                ('any_remark', models.CharField(max_length=100)),
                ('dialysis_type', models.CharField(max_length=100)),
                ('other_staff', models.CharField(max_length=100)),
                ('completion_status', models.CharField(max_length=100)),
                ('needle_type', models.CharField(max_length=100)),
                ('dialyser', models.CharField(max_length=100)),
                ('bundle_volume', models.CharField(max_length=100)),
                ('reprocess_number', models.CharField(max_length=100)),
                ('reprocessed_date', models.CharField(max_length=100)),
                ('rating', models.CharField(max_length=100)),
                ('single_used_dialyzer', models.CharField(max_length=100)),
                ('bp_sitting_max', models.CharField(max_length=50)),
                ('bp_sitting_min', models.CharField(max_length=50)),
                ('bp_standing_max', models.CharField(max_length=50)),
                ('bp_standing_min', models.CharField(max_length=50)),
                ('respiration', models.CharField(max_length=50)),
                ('pulse_sitting', models.CharField(max_length=50)),
                ('pulse_standing', models.CharField(max_length=50)),
                ('tempreture', models.CharField(max_length=50)),
                ('measured_wt', models.CharField(max_length=50)),
                ('wheelchair_wt', models.CharField(max_length=50)),
                ('prosthetic_wt', models.CharField(max_length=50)),
                ('condition_assessment', models.CharField(max_length=100)),
                ('assessment', models.CharField(max_length=100)),
                ('current_wt', models.CharField(max_length=100)),
                ('previous_wt', models.CharField(max_length=100)),
                ('weight_change', models.CharField(max_length=100)),
                ('dry_wt_date', models.CharField(max_length=100)),
                ('target_wt', models.CharField(max_length=100)),
                ('excess', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
                ('target_UF_Vol_kg', models.CharField(max_length=100)),
                ('target_UFR_vol_kg_hr', models.CharField(max_length=100)),
                ('anticoagulation', models.CharField(max_length=100)),
                ('heparin_type', models.CharField(max_length=100)),
                ('initial_dose', models.CharField(max_length=100)),
                ('interim_Dose', models.CharField(max_length=100)),
                ('total_heparin_bolus', models.CharField(max_length=100)),
                ('hourly', models.CharField(max_length=100)),
                ('unit_in_syringe', models.CharField(max_length=100)),
                ('dialysis_odometer_str_reading', models.CharField(max_length=100)),
                ('pre_dialysis_assessment', models.CharField(max_length=100)),
                ('notes_pre_dialysis_session', models.CharField(max_length=100)),
                ('fluids_volume_ml', models.CharField(max_length=100)),
            ],
        ),
    ]
