# Generated by Django 4.1.7 on 2023-04-18 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("testapp", "0242_item_issue_child_transfer_status_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="item_return_tocpc_child",
            name="stock_transfer",
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="item_return_tocpc_parent",
            name="stock_transfer",
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
