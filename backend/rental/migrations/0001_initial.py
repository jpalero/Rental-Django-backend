# Generated by Django 4.2.1 on 2023-05-24 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('full_name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('contact', models.IntegerField()),
                ('email', models.EmailField(max_length=50)),
                ('service', models.CharField(choices=[('Renter', 'Renter'), ('Rentee', 'Rentee')], max_length=20)),
            ],
        ),
    ]
