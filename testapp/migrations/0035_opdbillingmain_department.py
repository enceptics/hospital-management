# Generated by Django 4.0.1 on 2022-11-11 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0034_alter_centralisedadminview_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='opdbillingmain',
            name='department',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
