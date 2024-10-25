# Generated by Django 4.2.16 on 2024-10-24 11:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=100000)),
                ('posted_on', models.DateTimeField(verbose_name=datetime.datetime)),
                ('finder_no', models.CharField(max_length=10, unique=True)),
                ('finder_email', models.EmailField(max_length=254, unique=True)),
                ('state', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('image', models.BinaryField()),
            ],
        ),
    ]
