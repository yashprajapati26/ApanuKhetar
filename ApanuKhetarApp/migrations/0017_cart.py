# Generated by Django 2.2 on 2021-08-23 06:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ApanuKhetarApp', '0016_wishlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('qty', models.CharField(default='1', max_length=100)),
                ('price', models.CharField(default='', max_length=100)),
                ('total_price', models.CharField(default='', max_length=100)),
                ('status', models.CharField(default='pending', max_length=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ApanuKhetarApp.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ApanuKhetarApp.User')),
            ],
        ),
    ]