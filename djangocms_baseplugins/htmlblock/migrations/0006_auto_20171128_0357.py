# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-28 03:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('htmlblock', '0005_auto_20171128_0343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='htmlblock',
            name='published_from_date',
            field=models.DateTimeField(blank=True, default=None, null=True,
                                       verbose_name='Published from'),
        ),
        migrations.AlterField(
            model_name='htmlblock',
            name='published_until_date',
            field=models.DateTimeField(blank=True, default=None, null=True,
                                       verbose_name='Published until'),
        ),
    ]
