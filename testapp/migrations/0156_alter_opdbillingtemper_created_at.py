# Generated by Django 4.0.1 on 2023-03-08 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0155_cancelopdbillingmain_alter_centralisedadminview_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opdbillingtemper',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
