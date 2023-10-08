from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def draw_menu(menu):
    if menu:
        return mark_safe(render_menu(menu))


def render_menu(menu):
    html = f'<ul>'
    html += render_menu_item(menu)
    for child in menu.children.all():
        html += render_menu(child)
    html += '</ul>'
    return html


def render_menu_item(menu_item):
    html = f'<li>{menu_item.name}'
    return html







