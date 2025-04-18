# Generated by Django 4.1.2 on 2023-04-08 11:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0211_patient_feedback_ps_sales_return_parent_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory_itemmaster',
            name='department',
        ),
        migrations.RemoveField(
            model_name='inventory_itemmaster',
            name='tax',
        ),
        migrations.AddField(
            model_name='inventory_itemmaster',
            name='Gst',
            field=models.CharField(choices=[('10%', '10%'), ('18%', '18%'), ('22%', '22%'), ('28%', '28%')], default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tokencreations',
            name='Date',
            field=models.DateField(default=datetime.date(2023, 4, 8)),
        ),
    ]
