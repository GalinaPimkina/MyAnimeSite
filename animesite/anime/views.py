from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView

from .forms import AddAnimeForm
from .models import Anime, Genre, Producer, Tag, Years, Author, Studio

menu = [
    {'title': 'Каталог аниме', 'url_name': 'all_anime'},
    {'title': 'Аниме по годам', 'url_name': 'anime_years'},
    {'title': 'Аниме по жанрам', 'url_name': 'anime_genre'},
    {'title': 'Студии', 'url_name': 'anime_studio'},
    {'title': 'Добавить аниме', 'url_name': 'addanime'},
]

class AnimeHomePage(ListView):
    '''главная страница сайта, выводится список всех аниме/
    пока что практически аналог AllAnimePage, но будет изменена в дальнейшем'''

    model = Anime
    template_name = 'anime/index.html'
    context_object_name = 'all_anime'

    extra_context = {
        'title': 'Главная страница',
        'menu': menu,
    }

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Главная страница'
    #     context['menu'] = menu
    #     context['anime_all'] = Anime.objects.all()
    #     return context


class AllAnimePage(ListView):
    """ страница отображения всех имеющихсся на сайте тайтлов """

    model = Anime
    template_name = 'anime/show_all_anime.html'
    context_object_name = 'all_anime'

    extra_context = {
        'menu': menu,
        'title': 'Каталог аниме',
    }


def show_anime_page(request, anime_slug):
    """ страница с описанием конкретного аниме """

    anime_obj = get_object_or_404(Anime, slug=anime_slug)
    genre = Genre.objects.filter(genre__slug=anime_slug)
    producer = Producer.objects.filter(producer__slug=anime_slug)
    tag = Tag.objects.filter(tags__slug=anime_slug)
    studio = Studio.objects.filter(studio__slug=anime_slug)

    data = {
        'title': anime_obj.name_ru,
        'anime_obj': anime_obj,
        'genre': genre,
        'producer': producer,
        'tag': tag,
        'studio': studio,
        'menu': menu,
    }
    return render(request, 'anime/anime_page.html', context=data)


class GenrePage(ListView):
    ''' вывод страницы со списком всех имеющихся на сайте жанров аниме '''

    model = Genre
    template_name = 'anime/anime_genre.html'
    context_object_name = 'genre'

    extra_context = {
        'title': 'Жанры',
        'menu': menu,
    }


def show_genre_page(request, genre_slug):
    """ на страницу выводятся все аниме, соответствующие выбранному жанру """

    genre_obj = get_object_or_404(Genre, genre_slug=genre_slug)
    animies = Anime.objects.filter(genre=genre_obj)

    data = {
        'title': f'Жанр {genre_obj.name}',
        'genre_obj': genre_obj,
        'animies': animies,
        'menu': menu,
    }

    return render(request, 'anime/genre_page.html', context=data)


class YearsPage(ListView):
    ''' вывод страницы со списком всех имеющихся на сайте годами выпуска аниме '''

    model = Years
    template_name = 'anime/year_page.html'
    context_object_name = 'years'

    extra_context = {
        'title': 'Все года',
        'menu': menu,
    }


def show_year_page(request, year):
    year_obj = get_object_or_404(Years, years=year)
    animies = Anime.objects.filter(year=year_obj)

    data = {
        'title': f'Все аниме за {year_obj.years} г.',
        'year_obj': year_obj,
        'animies': animies,
        'menu': menu,
    }
    return render(request, 'anime/anime_year_page.html', context=data)


def show_producer_page(request, producer_slug):
    producer_obj = get_object_or_404(Producer, producer_slug=producer_slug)
    animies = Anime.objects.filter(producer=producer_obj)

    data = {
        'title': producer_obj.name,
        'producer_obj': producer_obj,
        'animies': animies,
        'menu': menu,
    }
    return render(request, 'anime/producer_page.html', context=data)


def show_author_page(request, author_slug):
    author_obj = get_object_or_404(Author, author_slug=author_slug)
    animies = Anime.objects.filter(author=author_obj)

    data = {
        'title': author_obj.name,
        'producer_obj': author_obj,
        'animies': animies,
        'menu': menu,
    }
    return render(request, 'anime/author_page.html', context=data)


def show_tag_page(request, tag_slug):
    tag_obj = get_object_or_404(Tag, tag_slug=tag_slug)
    animies = Anime.objects.filter(tag=tag_obj)

    data = {
        'title': tag_obj.tag,
        'tag_obj': tag_obj,
        'animies': animies,
        'menu': menu,
    }
    return render(request, 'anime/tag_page.html', context=data)


class StudioPage(ListView):
    ''' страница со списком студий, которые выпускали те или иные аниме '''

    model = Studio
    template_name = 'anime/anime_studio.html'
    context_object_name = 'studio'

    extra_context = {
        'title': 'Студии',
        'menu': menu,
    }


def show_studio_page(request, studio_slug):
    studio_obj = get_object_or_404(Studio, studio_slug=studio_slug)
    animies = Anime.objects.filter(studio=studio_obj)

    data = {
        'title': studio_obj.name,
        'tag_obj': studio_obj,
        'animies': animies,
        'menu': menu,
    }
    return render(request, 'anime/studio_page.html', context=data)

def addanime(request):
    if request.method == "POST":
        form = AddAnimeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = AddAnimeForm()

    data = {
        'menu': menu,
        'title': 'Добавить аниме',
        'form': form
    }

    return render(request, 'anime/addanime.html', data)
