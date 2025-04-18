# Generated by Django 5.0.4 on 2024-06-08 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0036_battery_capacity_battery_type_features_max_wattage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, choices=[('starter_kits', 'Starter Kits'), ('devices', 'Devices'), ('tanks', 'Tanks'), ('accessories', 'Accessories'), ('e-liquids', 'E-Liquids'), ('alternatives', 'Alternatives'), ('disposables', 'Disposables')], default='e-liquids', max_length=20, null=True),
        ),
    ]
