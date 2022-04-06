# Generated by Django 4.0.1 on 2022-04-06 20:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoundItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('day_found', models.DateField(default=datetime.date.today)),
                ('found_by', models.CharField(max_length=50)),
                ('contact_no', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='LostItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('day_lost', models.DateField(default=datetime.date.today)),
                ('lost_by', models.CharField(max_length=50)),
                ('contact_no', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
