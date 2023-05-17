# Generated by Django 4.2 on 2023-05-17 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_method', '0005_charge_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='charge',
            name='cvc',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='charge',
            name='exp_month',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='charge',
            name='exp_year',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='charge',
            name='number',
            field=models.CharField(max_length=50, null=True),
        ),
    ]