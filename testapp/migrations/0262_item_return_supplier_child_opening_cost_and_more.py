# Generated by Django 4.1.3 on 2023-04-25 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0261_alter_item_return_supplier_child_return_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item_return_supplier_child',
            name='opening_cost',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='item_return_supplier_child',
            name='total_cost',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='item_return_supplier_child',
            name='transaction_cost',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
