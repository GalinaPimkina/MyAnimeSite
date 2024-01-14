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
    }

    return render(request, 'anime/index.html', context=data)


def show_all_anime(request):
    anime = Anime.objects.all().order_by('name_ru')
    data = {
        'menu': menu,
        'anime': anime,
    }

    return render(request, 'anime/show_all_anime.html', context=data)