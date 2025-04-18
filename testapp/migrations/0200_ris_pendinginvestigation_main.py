# Generated by Django 3.2.6 on 2023-04-03 16:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testapp', '0199_auto_20230403_1059'),
    ]

    operations = [
        migrations.CreateModel(
            name='RIS_PendingInvestigation_main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_no', models.CharField(max_length=100)),
                ('test_id', models.CharField(max_length=100)),
                ('visit_no', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='testapp.locationmaster')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.servicemaster')),
                ('uhid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.patientsregistrationsallinone')),
            ],
        ),
    ]
