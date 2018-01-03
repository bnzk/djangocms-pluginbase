# coding: utf-8
from __future__ import unicode_literals

import re
from django.conf import settings

from djangocms_baseplugins.baseplugin import defaults
from djangocms_baseplugins.baseplugin.utils import build_baseplugin_fieldset


# thx to rouxcode!
VIDEOPLUGIN_REGEXES = (
    re.compile("^https?\:\/\/(www\.)?youtu\.be\/(?P<youtube_id>[^\/]*)\??.*$"),
    re.compile("^https?\:\/\/(www\.)?youtube\.(com|nl|ru).*v=(?P<youtube_id>.*)\&?.*$"),
    re.compile(r"^https?\:\/\/(www\.)?youtube\.(com|nl|ru)\/embed\/(?P<youtube_id>[^\/]*)\??.*$"),
    re.compile(r"^https?\:\/\/(www\.)?vimeo\.com\/(?P<vimeo_id>[^\/]*)\??.*$"),
)


VIDEOPLUGIN_LAYOUT_CHOICES = getattr(
    settings, 'VIDEOPLUGIN_LAYOUT_CHOICES', (
        [],
    )
)

VIDEOPLUGIN_CONTENT_FIELDS = getattr(
    settings, 'VIDEOPLUGIN_CONTENT_FIELDS', (
        'video_url', ('autoplay', 'controls', 'infos', 'fullscreen' ),
    )
)

VIDEOPLUGIN_DESIGN_FIELDS = getattr(
    settings, 'VIDEOPLUGIN_DESIGN_FIELDS', []
)

VIDEOPLUGIN_FIELDSETS = getattr(
    settings,
    'VIDEOPLUGIN_FIELDSETS',
    build_baseplugin_fieldset(**{
        'design': VIDEOPLUGIN_DESIGN_FIELDS,
        'content': VIDEOPLUGIN_CONTENT_FIELDS,
        'advanced': defaults.BASEPLUGIN_ADVANCED_FIELDS,
    })
)