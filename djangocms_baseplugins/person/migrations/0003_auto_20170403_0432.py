# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-04-03 04:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0002_auto_20161108_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='salutation',
            field=models.CharField(default='', max_length=255, verbose_name='Salutation'),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=64, verbose_name='phone'),
        ),
    ]
