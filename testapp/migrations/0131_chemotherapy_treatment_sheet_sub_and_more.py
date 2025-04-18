# Generated by Django 4.0.1 on 2023-01-31 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0130_chemotherapy_treatment_sheet_dialysis_details_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chemotherapy_treatment_sheet_sub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uhid', models.CharField(max_length=30)),
                ('date', models.CharField(max_length=100)),
                ('bp', models.CharField(max_length=100)),
                ('p_temp', models.CharField(max_length=100)),
                ('wht', models.CharField(max_length=100)),
                ('wbc', models.CharField(max_length=100)),
                ('hb', models.CharField(max_length=100)),
                ('plt', models.CharField(max_length=100)),
                ('uec', models.CharField(max_length=100)),
                ('remark1', models.CharField(max_length=100)),
                ('remark2', models.CharField(max_length=100)),
                ('remark3', models.CharField(max_length=100)),
                ('remark4', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='chemotherapy_treatment_sheet',
            name='bp',
        ),
        migrations.RemoveField(
            model_name='chemotherapy_treatment_sheet',
            name='date',
        ),
        migrations.RemoveField(
            model_name='chemotherapy_treatment_sheet',
            name='hb',
        ),
        migrations.RemoveField(
            model_name='chemotherapy_treatment_sheet',
            name='p_temp',
        ),
        migrations.RemoveField(
            model_name='chemotherapy_treatment_sheet',
            name='plt',
        ),
        migrations.RemoveField(
            model_name='chemotherapy_treatment_sheet',
            name='remark1',
        ),
        migrations.RemoveField(
            model_name='chemotherapy_treatment_sheet',
            name='remark2',
        ),
        migrations.RemoveField(
            model_name='chemotherapy_treatment_sheet',
            name='remark3',
        ),
        migrations.RemoveField(
            model_name='chemotherapy_treatment_sheet',
            name='remark4',
        ),
        migrations.RemoveField(
            model_name='chemotherapy_treatment_sheet',
            name='uec',
        ),
        migrations.RemoveField(
            model_name='chemotherapy_treatment_sheet',
            name='wbc',
        ),
        migrations.RemoveField(
            model_name='chemotherapy_treatment_sheet',
            name='wht',
        ),
        migrations.AddField(
            model_name='chemotherapy_treatment_sheet',
            name='uhid',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
