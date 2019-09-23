# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-09-21 16:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import filer_addons.filer_gui.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='poster_image',
            field=filer_addons.filer_gui.fields.FilerImageField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='video_video_image', to=settings.FILER_IMAGE_MODEL, verbose_name='Image'),
        ),
    ]