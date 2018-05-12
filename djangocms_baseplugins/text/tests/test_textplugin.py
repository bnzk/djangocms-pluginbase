from __future__ import unicode_literals

from django.test import TestCase
from django.test.client import RequestFactory
from cms.api import add_plugin
from cms.models import Placeholder
from cms.plugin_rendering import ContentRenderer
from django.utils.encoding import force_text

from djangocms_baseplugins.baseplugin.tests.base import BasePluginTestCase
from djangocms_baseplugins.text.cms_plugins import TextPlugin
from djangocms_baseplugins.text.models import Text


class TextPluginTests(BasePluginTestCase, TestCase):

    plugin_class = TextPlugin
    plugin_settings_prefix = 'TEXTPLUGIN'

    def test_plugin_html(self):
        placeholder = Placeholder.objects.create(slot='test')
        model_instance = add_plugin(
            placeholder,
            self.plugin_class,
            'en',
            **{
                'body': '<strong>Test</strong>',
            }
        )
        renderer = ContentRenderer(request=RequestFactory())
        html = renderer.render_plugin(model_instance, {})
        self.assertInHTML('<strong>Test</strong>', force_text(html))