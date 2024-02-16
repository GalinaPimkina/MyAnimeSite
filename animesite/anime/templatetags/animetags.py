from django import template
from anime.utils import menu

register = template.Library()

@register.simple_tag
def get_menu():
    return menu