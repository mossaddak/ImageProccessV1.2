# Generated by Django 4.2 on 2023-04-22 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_rename_filteer_png_imageprocess_filter_png'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageprocess',
            name='filter_jpg',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Filter Jpg'),
        ),
        migrations.AlterField(
            model_name='imageprocess',
            name='filter_png',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Filter Png'),
        ),
    ]
