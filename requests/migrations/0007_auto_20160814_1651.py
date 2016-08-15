# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-14 16:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0006_auto_20160805_1908'),
    ]

    operations = [
        migrations.RenameField(
            model_name='saleorder',
            old_name='document',
            new_name='documents',
        ),
        migrations.RemoveField(
            model_name='saleorder',
            name='delivery_type',
        ),
        migrations.RemoveField(
            model_name='saleorder',
            name='email',
        ),
        migrations.RemoveField(
            model_name='saleorder',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='saleorder',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='saleorder',
            name='message',
        ),
        migrations.RemoveField(
            model_name='saleorder',
            name='patronym',
        ),
        migrations.RemoveField(
            model_name='saleorder',
            name='phone',
        ),
    ]
