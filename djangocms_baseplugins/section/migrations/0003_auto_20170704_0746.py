# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-07-04 07:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('section', '0002_auto_20170704_0607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='anchor',
            field=models.SlugField(blank=True, default='', verbose_name='Anchor'),
        ),
        migrations.AlterField(
            model_name='section',
            name='background',
            field=models.CharField(blank=True, default='', max_length=64,
                                   verbose_name='Background'),
        ),
        migrations.AlterField(
            model_name='section',
            name='color',
            field=models.CharField(blank=True, default='', max_length=64, verbose_name='Color'),
        ),
        migrations.AlterField(
            model_name='section',
            name='in_menu',
            field=models.BooleanField(default=False, verbose_name='In Menu?'),
        ),
        migrations.AlterField(
            model_name='section',
            name='layout',
            field=models.CharField(blank=True, default='', max_length=64, verbose_name='Layout'),
        ),
        migrations.AlterField(
            model_name='section',
            name='published',
            field=models.BooleanField(default=True, verbose_name='Published?'),
        ),
        migrations.AlterField(
            model_name='section',
            name='title',
            field=models.CharField(blank=True, default='', max_length=256, verbose_name='Title'),
        ),
    ]
