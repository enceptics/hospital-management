# Generated by Django 4.1.7 on 2023-04-19 11:19

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ("testapp", "0248_alter_profilechargemaster_ward_category_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="transfer_request_mainstore_parent",
            name="item_issue_no",
            field=django_mysql.models.ListCharField(
                models.CharField(max_length=100),
                blank=True,
                max_length=1010,
                null=True,
                size=10,
            ),
        ),
    ]
