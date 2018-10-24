# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-11 10:06
from __future__ import unicode_literals

import cms.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('contentnav', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentnav',
            name='cms_page',
            field=cms.models.fields.PageField(default=None, help_text='Show submenu of this page', null=True, on_delete=django.db.models.deletion.CASCADE, to='cms.Page'),
        ),
        migrations.AddField(
            model_name='contentnav',
            name='menu_depth',
            field=models.PositiveIntegerField(default=1, verbose_name='Depth'),
        ),
        migrations.AddField(
            model_name='contentnav',
            name='sitemap',
            field=models.BooleanField(default=False, help_text='Show complete sitemap'),
        ),
    ]