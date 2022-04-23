# Generated by Django 3.1.7 on 2022-04-22 17:20

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(default='', max_length=200)),
                ('newspaper_name', models.CharField(default='', max_length=200)),
                ('title', models.TextField(default='')),
                ('summary', models.TextField(default='')),
                ('post_url', models.CharField(default='', max_length=200)),
                ('image_url', models.CharField(default='', max_length=200)),
                ('sentiment', models.FloatField()),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, size=None)),
                ('authors', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, size=None)),
            ],
        ),
    ]
