# Generated by Django 4.1.7 on 2023-04-12 10:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("testapp", "0224_timetaken_created_by_timetaken_location"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tokencreations",
            name="Date",
            field=models.DateField(default=datetime.date(2023, 4, 12)),
        ),
    ]
