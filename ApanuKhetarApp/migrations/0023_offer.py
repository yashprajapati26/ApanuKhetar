# Generated by Django 2.2 on 2021-08-27 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ApanuKhetarApp', '0022_delete_offer'),
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
                ('offer_Dicount_Price', models.CharField(max_length=10)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('ended_date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ApanuKhetarApp.Product')),
            ],
        ),
    ]
