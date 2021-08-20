# Generated by Django 2.2 on 2021-08-19 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=30)),
                ('LastName', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=50)),
                ('Password', models.CharField(max_length=20)),
            ],
        ),
    ]
