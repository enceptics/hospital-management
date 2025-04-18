# Generated by Django 4.0.1 on 2022-12-02 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0060_opdbillinggetdelete'),
        ('IPDapp', '0006_ipd_dept_doctor_transfer_bed_transfer'),
    ]

    operations = [
        migrations.AddField(
            model_name='admissioninfos',
            name='admission_ID',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='admissioninfos',
            name='bed_no',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='IPDapp.bedmastermain'),
        ),
        migrations.AlterField(
            model_name='admissioninfos',
            name='department',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='department', to='IPDapp.ipd_dept'),
        ),
        migrations.AlterField(
            model_name='admissioninfos',
            name='primary_doctor',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='primary_doctor', to='testapp.doctortable'),
        ),
        migrations.AlterField(
            model_name='admissioninfos',
            name='ref_hospital',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='testapp.hospitalmaster'),
        ),
        migrations.AlterField(
            model_name='admissioninfos',
            name='req_ward_cate',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='IPDapp.admissionwardcate'),
        ),
        migrations.AlterField(
            model_name='admissioninfos',
            name='req_ward_type',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='IPDapp.admissionwardtype'),
        ),
        migrations.AlterField(
            model_name='admissioninfos',
            name='secondary_doctor',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='secoundry_doctor', to='testapp.doctortable'),
        ),
    ]
