# Generated by Django 4.1.7 on 2023-04-19 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("testapp", "0247_opdbillingsub_order_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profilechargemaster",
            name="ward_category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="testapp.servicesubcategory",
            ),
        ),
        migrations.AlterField(
            model_name="profilechargemaster",
            name="ward_type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="testapp.servicecategory",
            ),
        ),
        migrations.AlterField(
            model_name="servicechargemaster",
            name="ward_category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="testapp.servicesubcategory",
            ),
        ),
        migrations.AlterField(
            model_name="servicechargemaster",
            name="ward_type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="testapp.servicecategory",
            ),
        ),
    ]
