# Generated by Django 5.0.4 on 2024-06-05 13:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_product_banner_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner_list',
            name='banner_1',
            field=models.ForeignKey(default='', limit_choices_to=True, on_delete=django.db.models.deletion.CASCADE, related_name='Banner_1', to='blog.product'),
        ),
    ]
