# -*- coding: utf-8
import logging
import os
import importlib
from django.apps import AppConfig
from dj_n3_templateplugins.plugin import TemplatePlugin


LOGGER = logging.getLogger(__name__)


class DjN3TemplatepluginsConfig(AppConfig):
    name = 'dj_n3_templateplugins'

    def ready(self):
        super().ready()
        self.load_plugins()

    def load_plugins(self):
        from .models import Plugin
        LOGGER.debug('loading plugins')
        PLUGIN_DIR = '/etc/dj_n3_templateplugins'
        directory = os.listdir(PLUGIN_DIR)
        LOGGER.debug('checking plugin_dir %s', PLUGIN_DIR)
        for f in directory:
            path = os.path.join(PLUGIN_DIR, f)
            if os.path.isdir(path):
                LOGGER.debug('loading plugin %s', f)
                pythonpath = '{}/{}/plugin.py'.format(PLUGIN_DIR, f)
                pmod = importlib.import_module(pythonpath)

                if self.validate_plugin(pmod.Plugin):
                    plugin, created = Plugin.objects.get_or_create(name=f, defaults={
                        'pythonpath': pythonpath
                    })
                    LOGGER.info('get_or_create, created: %s, plugin: %s:%s', created, plugin.name, plugin.status)
                else:
                    LOGGER.warning('Plugin must be a valid plugin, did you inherit from plugin.TemplatePlugin?')

    def validate_plugin(self, cls):
        """Validate that the given class is a proper dj_n3_templateplugin

        Args:
            cls (Class):  the plugin class to be loaded

        Returns:
            bool: True if valid, False if not.

        """
        return isinstance(cls(), TemplatePlugin)

