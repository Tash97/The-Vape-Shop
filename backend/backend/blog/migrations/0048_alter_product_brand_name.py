# Generated by Django 5.0.4 on 2024-06-11 07:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0047_alter_product_brand_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand_name',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='BrandName', to='blog.brand'),
        ),
    ]
