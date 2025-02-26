# Generated by Django 2.2.5 on 2019-11-13 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unisport_id', models.IntegerField(blank=True)),
                ('brand', models.CharField(blank=True, max_length=255)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('image', models.URLField(blank=True, max_length=2000)),
                ('url', models.URLField(blank=True, max_length=2000)),
                ('price', models.IntegerField(blank=True)),
                ('currency', models.CharField(blank=True, max_length=10)),
                ('discount', models.IntegerField(blank=True)),
                ('delivery', models.CharField(blank=True, max_length=255)),
                ('labels', models.CharField(blank=True, max_length=255)),
                ('sizes', models.TextField(blank=True, max_length=1000)),
                ('description', models.TextField(blank=True)),
                ('age', models.CharField(blank=True, max_length=255)),
                ('gender', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
