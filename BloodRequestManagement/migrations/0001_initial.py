# Generated by Django 4.2.8 on 2024-01-06 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BloodRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requester_name', models.CharField(max_length=255)),
                ('contact_email', models.EmailField(max_length=254)),
                ('hospital', models.CharField(max_length=255)),
                ('town', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('blood_type', models.CharField(max_length=10)),
                ('units', models.IntegerField()),
                ('duration_of_search_days', models.IntegerField()),
                ('reason', models.TextField()),
            ],
        ),
    ]