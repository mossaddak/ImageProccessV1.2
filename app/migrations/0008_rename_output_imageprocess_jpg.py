# Generated by Django 4.2 on 2023-04-21 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_imageprocess_output'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imageprocess',
            old_name='output',
            new_name='jpg',
        ),
    ]
