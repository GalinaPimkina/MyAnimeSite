from django import template
from anime.models import Genre

register = template.Library()

@register.simple_tag()
def get_genre():
    genre = Genre.objects.all()
    lst = []
    for g in genre:
        lst.append(g)

    return lst