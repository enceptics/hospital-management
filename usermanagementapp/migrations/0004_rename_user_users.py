# Generated by Django 4.0.1 on 2022-12-26 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagementapp', '0003_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Users',
        ),
    ]
