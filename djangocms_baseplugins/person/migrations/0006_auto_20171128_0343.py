# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-28 03:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0005_auto_20170704_0746'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='published_from_date',
            field=models.DateTimeField(default=None, null=True, verbose_name='Published from'),
        ),
        migrations.AddField(
            model_name='person',
            name='published_until_date',
            field=models.DateTimeField(default=None, null=True, verbose_name='Published until'),
        ),
        migrations.AddField(
            model_name='personsection',
            name='published_from_date',
            field=models.DateTimeField(default=None, null=True, verbose_name='Published from'),
        ),
        migrations.AddField(
            model_name='personsection',
            name='published_until_date',
            field=models.DateTimeField(default=None, null=True, verbose_name='Published until'),
        ),
    ]