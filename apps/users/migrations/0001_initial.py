# Generated by Django 4.2.5 on 2023-09-22 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='имя')),
                ('last_name', models.CharField(max_length=255, verbose_name='фамилия')),
                ('age', models.IntegerField(max_length=3, verbose_name='возраст')),
                ('phone_number', models.CharField(max_length=20, verbose_name='телефонный номер')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
            ],
        ),
    ]
