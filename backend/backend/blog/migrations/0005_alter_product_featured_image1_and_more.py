# Generated by Django 5.0.4 on 2024-06-03 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_product_product_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='featured_image1',
            field=models.ImageField(blank=True, default='', upload_to='product/main_images/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='featured_image2',
            field=models.ImageField(blank=True, default='', upload_to='product/main_images/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='featured_image3',
            field=models.ImageField(blank=True, default='', upload_to='product/main_images/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='featured_image4',
            field=models.ImageField(blank=True, default='', upload_to='product/main_images/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='featured_image5',
            field=models.ImageField(blank=True, default='', upload_to='product/main_images/%Y/%m/%d/'),
        ),
    ]
