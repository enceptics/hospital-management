# Generated by Django 4.0.1 on 2023-02-04 12:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0138_delete_estimate_bill_main'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory_ItemMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belongs_to', models.CharField(max_length=100)),
                ('item_category', models.CharField(max_length=100)),
                ('item_subcategory', models.CharField(max_length=100)),
                ('item_name', models.CharField(max_length=100)),
                ('shortcode', models.CharField(max_length=100)),
                ('packing', models.CharField(max_length=100)),
                ('contain', models.CharField(max_length=100)),
                ('unit', models.CharField(max_length=100)),
                ('conversion_factor', models.CharField(max_length=100)),
                ('hsn_code', models.CharField(max_length=100)),
                ('hsn_item_code', models.CharField(max_length=100)),
                ('remark', models.CharField(max_length=100)),
                ('Gst', models.CharField(choices=[('10%', '10%'), ('18%', '18%'), ('22%', '22%'), ('28%', '28%')], max_length=100)),
                ('num_of_reuse', models.CharField(max_length=100)),
                ('serial_batch_control', models.CharField(max_length=100)),
                ('reusable_rate', models.CharField(max_length=100)),
                ('min_quantity', models.CharField(max_length=100)),
                ('max_quantity', models.CharField(max_length=100)),
                ('re_order_level', models.CharField(max_length=100)),
                ('status', models.CharField(blank=True, max_length=100)),
                ('assets', models.CharField(blank=True, max_length=100)),
                ('expiry', models.CharField(max_length=100)),
                ('create_by', models.DateField()),
                ('updated_by', models.DateField()),
                ('is_reusable', models.CharField(max_length=100)),
                ('tpa', models.CharField(max_length=100)),
                ('service_charge', models.CharField(max_length=100)),
                ('autointent', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='centralisedadminview',
            name='Date',
            field=models.DateField(default=datetime.date(2023, 2, 4)),
        ),
        migrations.AlterField(
            model_name='tokencreationdone',
            name='Date',
            field=models.DateField(default=datetime.date(2023, 2, 4)),
        ),
        migrations.AlterField(
            model_name='tokencreations',
            name='Date',
            field=models.DateField(default=datetime.date(2023, 2, 4)),
        ),
    ]
