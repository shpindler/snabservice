# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-04 22:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20160730_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancie',
            name='salary',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='vacancie',
            name='schedule',
            field=models.CharField(max_length=50),
        ),
    ]
