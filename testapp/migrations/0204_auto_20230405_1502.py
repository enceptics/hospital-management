# Generated by Django 3.2.6 on 2023-04-05 15:02

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0203_auto_20230404_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tokencreations',
            name='Date',
            field=models.DateField(default=datetime.date(2023, 4, 5)),
        ),
        migrations.CreateModel(
            name='TemplateMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('status', models.CharField(max_length=100)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.servicemaster')),
            ],
        ),
    ]
