# Generated by Django 2.2 on 2021-08-28 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ApanuKhetarApp', '0024_auto_20210828_1506'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='After_Discount',
        ),
        migrations.RemoveField(
            model_name='product',
            name='Final_Amount',
        ),
        migrations.RemoveField(
            model_name='product',
            name='Tax_Amount',
        ),
        migrations.RemoveField(
            model_name='product',
            name='Tax_Percentage',
        ),
    ]
