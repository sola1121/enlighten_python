# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-24 06:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_author_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=15)),
                ('website', models.URLField()),
            ],
        ),
    ]
