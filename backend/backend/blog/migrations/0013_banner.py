# Generated by Django 5.0.4 on 2024-06-05 08:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_remove_featured_list_featured_product_1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_picture', models.ImageField(blank=True, default='', upload_to='banners/%Y/%m/%d/')),
                ('banner_product', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='blog.product')),
            ],
        ),
    ]
