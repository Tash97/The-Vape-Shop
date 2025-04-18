# Generated by Django 5.0.4 on 2024-06-04 11:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_product_featured_image1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Featured',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('featured1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.product')),
            ],
            options={
                'verbose_name': 'featured',
                'verbose_name_plural': '3. Featured List',
            },
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
