# Generated by Django 2.2 on 2021-08-20 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApanuKhetarApp', '0008_auto_20210820_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='After_Discount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='Discount_Amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='Discount_Percentage',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='Final_Amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='Product_Quantity',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='Product_image_2',
            field=models.ImageField(blank=True, null=True, upload_to='Product_Images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Product_image_3',
            field=models.ImageField(blank=True, null=True, upload_to='Product_Images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Product_image_4',
            field=models.ImageField(blank=True, null=True, upload_to='Product_Images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Tax_Amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='Tax_Percentage',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
