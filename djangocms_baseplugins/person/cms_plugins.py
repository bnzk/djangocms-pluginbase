# coding: utf-8
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from djangocms_baseplugins.baseplugin.cms_plugins import BasePluginMixin
from .models import Person
from djangocms_baseplugins.section.models import Section

from . import conf


class PersonSectionPlugin(BasePluginMixin, CMSPluginBase):
    model = Section
    module = _("containers")
    name = _(u'person section')
    render_template = "person/person_section.html"
    allow_children = True
    child_classes = ('PersonPlugin', )
    fieldsets = conf.PERSONSECTIONPLUGIN_FIELDSETS

plugin_pool.register_plugin(PersonSectionPlugin)


class PersonPlugin(BasePluginMixin, CMSPluginBase):
    model = Person
    name = _(u'person')
    render_template = "person/person.html"
    require_parent = True
    fieldsets = conf.PERSONPLUGIN_FIELDSETS

plugin_pool.register_plugin(PersonPlugin)