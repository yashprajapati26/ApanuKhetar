# Generated by Django 2.2 on 2021-08-28 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ApanuKhetarApp', '0023_offer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Discount_Amount',
        ),
        migrations.RemoveField(
            model_name='product',
            name='Discount_Percentage',
        ),
    ]
