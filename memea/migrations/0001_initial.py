# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 09:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Memea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('izenburua', models.CharField(max_length=100)),
                ('argazkia', models.CharField(max_length=200)),
            ],
        ),
    ]