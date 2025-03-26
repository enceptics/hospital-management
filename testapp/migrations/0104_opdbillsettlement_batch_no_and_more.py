# Generated by Django 4.0.1 on 2022-12-29 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0103_patientvisitmains_batch_no_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='opdbillsettlement',
            name='batch_no',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='opdbillsettlement',
            name='claim_no',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='opdbillsettlement',
            name='refrence_id',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='opdbillsettlementtemp',
            name='batch_no',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='opdbillsettlementtemp',
            name='claim_no',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='opdbillsettlementtemp',
            name='refrence_id',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
