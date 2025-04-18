# Generated by Django 3.2.6 on 2023-04-04 10:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testapp', '0200_ris_pendinginvestigation_main'),
    ]

    operations = [
        migrations.AddField(
            model_name='ris_pendinginvestigation_main',
            name='status',
            field=models.CharField(default='active', max_length=100),
        ),
        migrations.AlterField(
            model_name='tokencreations',
            name='Date',
            field=models.DateField(default=datetime.date(2023, 4, 4)),
        ),
        migrations.CreateModel(
            name='RIS_report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discerption', models.TextField()),
                ('conclusion', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('RIS_PendingInvestigation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.ris_pendinginvestigation_main')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='testapp.locationmaster')),
            ],
        ),
    ]
