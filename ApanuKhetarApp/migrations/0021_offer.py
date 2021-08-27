# Generated by Django 2.2 on 2021-08-27 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ApanuKhetarApp', '0020_auto_20210827_1132'),
    ]

    operations = [
        migrations.CreateModel(
            name='offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer_name', models.CharField(max_length=30)),
                ('offer_status', models.CharField(choices=[('Active', 'Active'), ('Deactive', 'Deactive')], default='Active', max_length=10)),
                ('offer_dicription', models.CharField(max_length=300)),
                ('offer_Dicount_Percentage', models.CharField(max_length=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ApanuKhetarApp.Product')),
            ],
        ),
    ]