# Generated by Django 5.0.4 on 2024-06-11 03:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0043_product_disposable_ejuice_capacity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='battery_type',
            name='option',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='device_battery_type',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='BatteryType', to='blog.battery_type'),
        ),
    ]
