# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-09-21 16:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0004_auto_20190921_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='show_related',
            field=models.BooleanField(default=False, verbose_name='show related'),
        ),
    ]
