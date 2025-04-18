# Generated by Django 4.0.1 on 2022-12-24 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('IPDapp', '0007_admissioninfos_admission_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMangement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=1000)),
                ('patient_registration_add', models.BooleanField()),
                ('patient_registration_edit', models.BooleanField()),
                ('patient_registration_register_card', models.BooleanField()),
                ('patient_registration_visiter', models.BooleanField()),
                ('ipd_save', models.BooleanField()),
                ('ipd_edit', models.BooleanField()),
                ('ipd_print_QR_code', models.BooleanField()),
                ('ipd_discharge', models.BooleanField()),
                ('ipd_admission_slip', models.BooleanField()),
                ('ipd_admission_form', models.BooleanField()),
                ('ipd_stickers', models.BooleanField()),
                ('ipd_bed_transfer', models.BooleanField()),
                ('title_master_add', models.BooleanField()),
                ('title_master_edit', models.BooleanField()),
                ('title_master_view', models.BooleanField()),
                ('hospital_master_add', models.BooleanField()),
                ('hospital_master_edit', models.BooleanField()),
                ('hospital_master_view', models.BooleanField()),
                ('holiday_master_add', models.BooleanField()),
                ('holiday_master_edit', models.BooleanField()),
                ('holiday_master_view', models.BooleanField()),
                ('gender_master_add', models.BooleanField()),
                ('gender_master_edit', models.BooleanField()),
                ('gender_master_view', models.BooleanField()),
                ('district_master_add', models.BooleanField()),
                ('district_master_edit', models.BooleanField()),
                ('district_master_view', models.BooleanField()),
                ('country_master_add', models.BooleanField()),
                ('country_master_edit', models.BooleanField()),
                ('country_master_view', models.BooleanField()),
                ('city_master_add', models.BooleanField()),
                ('city_master_edit', models.BooleanField()),
                ('city_master_view', models.BooleanField()),
                ('most_document_add', models.BooleanField()),
                ('most_document_edit', models.BooleanField()),
                ('most_document_view', models.BooleanField()),
                ('Martial_status_add', models.BooleanField()),
                ('Martial_status_edit', models.BooleanField()),
                ('Martial_status_view', models.BooleanField()),
                ('relation_master_add', models.BooleanField()),
                ('relation_master_edit', models.BooleanField()),
                ('relation_master_view', models.BooleanField()),
                ('group_master_add', models.BooleanField()),
                ('group_master_edit', models.BooleanField()),
                ('group_master_view', models.BooleanField()),
                ('room_master_add', models.BooleanField()),
                ('room_master_edit', models.BooleanField()),
                ('room_master_view', models.BooleanField()),
                ('branch_master_add', models.BooleanField()),
                ('branch_master_edit', models.BooleanField()),
                ('branch_master_view', models.BooleanField()),
                ('visit_type_master_add', models.BooleanField()),
                ('visit_type_master_edit', models.BooleanField()),
                ('visit_type_master_view', models.BooleanField()),
                ('service_category_add', models.BooleanField()),
                ('service_category_edit', models.BooleanField()),
                ('service_category_view', models.BooleanField()),
                ('service_sub_category_add', models.BooleanField()),
                ('service_sub_category_edit', models.BooleanField()),
                ('service_sub_category_view', models.BooleanField()),
                ('service_department_add', models.BooleanField()),
                ('service_department_edit', models.BooleanField()),
                ('service_department_view', models.BooleanField()),
                ('service_sub_department_add', models.BooleanField()),
                ('service_sub_department_edit', models.BooleanField()),
                ('service_sub_department_view', models.BooleanField()),
                ('ward_add', models.BooleanField()),
                ('ward_edit', models.BooleanField()),
                ('ward_view', models.BooleanField()),
                ('ward_category_add', models.BooleanField()),
                ('ward_category_edit', models.BooleanField()),
                ('ward_category_view', models.BooleanField()),
                ('blood_master_add', models.BooleanField()),
                ('blood_master_edit', models.BooleanField()),
                ('blood_master_view', models.BooleanField()),
                ('clinical_department_add', models.BooleanField()),
                ('clinical_department_edit', models.BooleanField()),
                ('clinical_department_view', models.BooleanField()),
                ('desgination_add', models.BooleanField()),
                ('desgination_edit', models.BooleanField()),
                ('desgination_view', models.BooleanField()),
                ('sevice_add', models.BooleanField()),
                ('sevice_search', models.BooleanField()),
                ('wing_master_add', models.BooleanField()),
                ('wing_master_edit', models.BooleanField()),
                ('wing_master_view', models.BooleanField()),
                ('floor_master_add', models.BooleanField()),
                ('floor_master_edit', models.BooleanField()),
                ('floor_master_view', models.BooleanField()),
                ('ipd_room_master_add', models.BooleanField()),
                ('ipd_room_master_edit', models.BooleanField()),
                ('ipd_room_master_view', models.BooleanField()),
                ('bed_master_add', models.BooleanField()),
                ('bed_master_edit', models.BooleanField()),
                ('bed_master_view', models.BooleanField()),
                ('ward_type_add', models.BooleanField()),
                ('ward_type_edit', models.BooleanField()),
                ('ward_type_view', models.BooleanField()),
                ('ipd_ward_category_add', models.BooleanField()),
                ('ipd_ward_category_edit', models.BooleanField()),
                ('ipd_ward_category_view', models.BooleanField()),
                ('ward_name_add', models.BooleanField()),
                ('ward_name_edit', models.BooleanField()),
                ('ward_name_view', models.BooleanField()),
                ('bed_location_add', models.BooleanField()),
                ('bed_location_edit', models.BooleanField()),
                ('bed_location_view', models.BooleanField()),
                ('nursing_counter_add', models.BooleanField()),
                ('nursing_counter_edit', models.BooleanField()),
                ('nursing_counter_view', models.BooleanField()),
                ('ipd_department_add', models.BooleanField()),
                ('ipd_department_edit', models.BooleanField()),
                ('ipd_department_view', models.BooleanField()),
                ('room_defination_add', models.BooleanField()),
                ('room_defination_edit', models.BooleanField()),
                ('room_defination_view', models.BooleanField()),
                ('billing_group_traiff_add', models.BooleanField()),
                ('billing_group_traiff_edit', models.BooleanField()),
                ('billing_group_traiff_view', models.BooleanField()),
                ('tariff_charge_master_add', models.BooleanField()),
                ('tariff_charge_master_edit', models.BooleanField()),
                ('tariff_charge_master_view', models.BooleanField()),
                ('tariff_master_add', models.BooleanField()),
                ('tariff_master_edit', models.BooleanField()),
                ('tariff_master_view', models.BooleanField()),
                ('corporate_master_add', models.BooleanField()),
                ('corporate_master_edit', models.BooleanField()),
                ('corporate_master_view', models.BooleanField()),
                ('billing_group_master_add', models.BooleanField()),
                ('billing_group_master_edit', models.BooleanField()),
                ('billing_group_master_view', models.BooleanField()),
                ('cop_billing_linking_add', models.BooleanField()),
                ('cop_billing_linking_edit', models.BooleanField()),
                ('cop_billing_linking_view', models.BooleanField()),
                ('item_master_add', models.BooleanField()),
                ('item_master_edit', models.BooleanField()),
                ('item_master_view', models.BooleanField()),
                ('item_category_master_add', models.BooleanField()),
                ('item_category_master_edit', models.BooleanField()),
                ('item_category_master_view', models.BooleanField()),
                ('item_belong_master_add', models.BooleanField()),
                ('item_belong_master_edit', models.BooleanField()),
                ('item_belong_master_view', models.BooleanField()),
                ('packaging_add', models.BooleanField()),
                ('packaging_edit', models.BooleanField()),
                ('packaging_view', models.BooleanField()),
                ('item_unit_master_add', models.BooleanField()),
                ('item_unit_master_edit', models.BooleanField()),
                ('item_unit_master_view', models.BooleanField()),
                ('item_manufacture_add', models.BooleanField()),
                ('item_manufacture_edit', models.BooleanField()),
                ('item_manufacture_view', models.BooleanField()),
                ('store_master_add', models.BooleanField()),
                ('store_master_edit', models.BooleanField()),
                ('store_master_view', models.BooleanField()),
                ('vendor_master_add', models.BooleanField()),
                ('vendor_master_view', models.BooleanField()),
                ('vendor_master_edit', models.BooleanField()),
                ('store_nursing_counter_add', models.BooleanField()),
                ('store_nursing_counter_edit', models.BooleanField()),
                ('store_nursing_counter_view', models.BooleanField()),
                ('item_location_add', models.BooleanField()),
                ('item_location_edit', models.BooleanField()),
                ('item_location_view', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='UserMangement_ward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=1000)),
                ('ward_cat', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Dummy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ward_cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IPDapp.admissionwardcate')),
            ],
        ),
    ]
