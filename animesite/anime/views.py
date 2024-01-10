from django.shortcuts import render

from .models import Anime

menu = [
    {'title': 'Каталог аниме', 'url_name': 'all_anime'},
    {'title': 'Аниме по годам', 'url_name': 'anime_years'},
    {'title': 'Аниме по жанрам', 'url_name': 'anime_genre'},
    {'title': 'Студии', 'url_name': 'anime_studio'},
]

def index(request):
    anime_all = Anime.objects.all()
    data = {
        'title': 'Главная страница',
        'anime_all': anime_all,
        'menu': menu,
    }

    return render(request, 'anime/index.html', context=data)