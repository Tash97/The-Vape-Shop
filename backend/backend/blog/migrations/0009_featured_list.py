# Generated by Django 5.0.4 on 2024-06-05 00:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_delete_carousellist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Featured_List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('featured_list_name', models.CharField(max_length=100)),
                ('featured_product_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.product')),
            ],
        ),
    ]
