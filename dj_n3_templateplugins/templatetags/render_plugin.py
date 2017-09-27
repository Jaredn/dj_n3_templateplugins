from django.template import Library, Context, Template
import importlib
from dj_n3_templateplugins.utils import get_plugin_instance


register = Library()


@register.simple_tag(takes_context=True)
def render_plugin(context, plugin_obj):
    plugin_instance = get_plugin_instance(plugin_obj)
    plugin_context = plugin_instance.get_context_data()
    context['plugin_local'][plugin_obj.name] = plugin_context
    t = Template(plugin_instance.render_html())
    return t.render(Context(context))
