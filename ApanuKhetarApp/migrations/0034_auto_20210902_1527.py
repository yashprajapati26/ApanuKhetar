# Generated by Django 2.2 on 2021-09-02 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApanuKhetarApp', '0033_auto_20210902_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='ended_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='offer',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]
