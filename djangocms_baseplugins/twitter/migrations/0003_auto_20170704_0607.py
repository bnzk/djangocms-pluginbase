# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-07-04 06:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('twitter', '0002_auto_20161108_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweetembed',
            name='background',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='tweetembed',
            name='color',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='tweetembed',
            name='layout',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
    ]
