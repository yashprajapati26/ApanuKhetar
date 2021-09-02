# Generated by Django 2.2 on 2021-09-02 04:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ApanuKhetarApp', '0031_remove_user_dob'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('message', models.CharField(max_length=100)),
                ('added_date', models.DateField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ApanuKhetarApp.Product')),
            ],
        ),
    ]
