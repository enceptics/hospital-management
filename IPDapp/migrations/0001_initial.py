# Generated by Django 4.0.1 on 2022-05-20 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('testapp', '0006_alter_centralisedadminview_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdmissionWardCate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AdmissionWardType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ward_type', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BedLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FloorMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floor_name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NursingStationCounter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counter_name', models.CharField(max_length=100, unique=True)),
                ('inactive', models.BooleanField()),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WardName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ward_name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WingMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wing_name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RoomMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField(max_length=40)),
                ('description', models.TextField(blank=True, null=True)),
                ('floor_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IPDapp.floormaster')),
                ('wing_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IPDapp.wingmaster')),
            ],
        ),
        migrations.CreateModel(
            name='RoomDefination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], max_length=20)),
                ('bed_charge_not_applicable', models.BooleanField()),
                ('inactive', models.BooleanField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department', to='IPDapp.department')),
                ('floor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='floor', to='IPDapp.floormaster')),
                ('nursing_counter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nursecounter', to='IPDapp.nursingstationcounter')),
                ('room_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room', to='testapp.roomnumber')),
                ('ward_cate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wardcate', to='IPDapp.admissionwardcate')),
                ('ward_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wardname', to='IPDapp.wardname')),
                ('ward_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wardtype', to='IPDapp.admissionwardtype')),
                ('wing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wing', to='IPDapp.wingmaster')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='IPDapp.city')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='IPDapp.country')),
            ],
        ),
        migrations.AddField(
            model_name='floormaster',
            name='wing_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IPDapp.wingmaster'),
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IPDapp.country'),
        ),
        migrations.CreateModel(
            name='BedMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bed_no', models.CharField(max_length=30)),
                ('bed_location', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('floor_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IPDapp.floormaster')),
                ('room_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IPDapp.roommaster')),
                ('wing_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IPDapp.wingmaster')),
            ],
        ),
        migrations.CreateModel(
            name='BedAllotments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bed_id', models.CharField(max_length=20, unique=True)),
                ('bed_nos', models.CharField(max_length=20, unique=True)),
                ('room_nos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.roomnumber')),
            ],
        ),
        migrations.CreateModel(
            name='AdmissionWardCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ward_category', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('ward_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IPDapp.admissionwardtype')),
            ],
        ),
        migrations.CreateModel(
            name='AdmissionInfos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uhid', models.CharField(max_length=50)),
                ('admission_datetime', models.DateTimeField(auto_now_add=True)),
                ('admission_type', models.CharField(choices=[('Normal Admission', 'Normal Admission'), ('Emergency Admission', 'Emergency Admission'), ('Online Admission', 'Online Admission'), ('Offline Admission', 'Offline Admission')], max_length=50)),
                ('infected', models.BooleanField()),
                ('MLC', models.BooleanField()),
                ('MLC_No', models.CharField(blank=True, max_length=50, null=True)),
                ('bed_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IPDapp.bedallotments')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department', to='testapp.doctortable')),
                ('primary_doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='primary_doctor', to='testapp.doctortable')),
                ('ref_hospital', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='testapp.hospitalmaster')),
                ('req_ward_cate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='IPDapp.admissionwardcategory')),
                ('req_ward_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='IPDapp.admissionwardtype')),
                ('secondary_doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='secoundry_doctor', to='testapp.doctortable')),
            ],
        ),
    ]
