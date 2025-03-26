# Generated by Django 3.2.6 on 2023-03-18 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagementapp', '0006_screenaccess_usermangement_main'),
        ('testapp', '0173_auto_20230318_0939'),
    ]

    operations = [
        migrations.AddField(
            model_name='createuser',
            name='user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='create_user_profile', to='usermanagementapp.screenaccess'),
        ),
    ]
