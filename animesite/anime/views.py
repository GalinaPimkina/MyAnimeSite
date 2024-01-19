from django.shortcuts import render, get_object_or_404

from .models import Anime, Genre, Producer, Tag

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


def show_anime_page(request, anime_slug):
    anime_obj = get_object_or_404(Anime, slug=anime_slug)
    genre = Genre.objects.filter(genre__slug=anime_obj.slug)
    producer = Producer.objects.filter(producer__slug=anime_slug)
    tag = Tag.objects.filter(tags__slug=anime_slug)

    data = {
        'title': anime_obj.name_ru,
        'anime_obj': anime_obj,
        'genre': genre,
        'producer': producer,
        'tag': tag,
        'menu': menu,
    }
    return render(request, 'anime/anime_page.html', context=data)


def anime_genre(request):
    genre = Genre.objects.all().order_by('name')

    data = {
        'title': 'Жанры',
        'genre': genre,
        'menu': menu,
    }

    return render(request, 'anime/anime_genre.html', context=data)