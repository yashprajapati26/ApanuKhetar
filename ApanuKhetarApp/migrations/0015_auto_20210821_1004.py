# Generated by Django 2.2 on 2021-08-21 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApanuKhetarApp', '0014_auto_20210821_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Product_image_2',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='Product_Images/'),
        ),
    ]
