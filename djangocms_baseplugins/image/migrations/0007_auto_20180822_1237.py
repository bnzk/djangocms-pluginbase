# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-08-22 12:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import filer_addons.filer_gui.fields


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0006_auto_20171128_0357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=filer_addons.filer_gui.fields.FilerImageField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='image_image_image', to=settings.FILER_IMAGE_MODEL, verbose_name='Image'),
        ),
    ]