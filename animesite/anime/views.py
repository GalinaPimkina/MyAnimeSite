from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView

from .forms import AddAnimeForm
from .models import Anime, Genre, Producer, Tag, Years, Author, Studio

menu = [
    {'title': 'Каталог аниме', 'url_name': 'all_anime_page'},
    {'title': 'Аниме по годам', 'url_name': 'year_page'},
    {'title': 'Аниме по жанрам', 'url_name': 'genre_page'},
    {'title': 'Студии', 'url_name': 'anime_studio'},
    {'title': 'Добавить аниме', 'url_name': 'addanime'},
]

class AnimeHomePageView(ListView):
    '''главная страница сайта, выводится список всех аниме/
    пока что практически аналог AllAnimePage, но будет изменена в дальнейшем'''

    model = Anime
    template_name = 'anime/anime_home_page.html'
    context_object_name = 'anime'

    extra_context = {
        'title': 'Главная страница',
        'menu': menu,
    }


class AllAnimePageView(ListView):
    """ страница отображения всех имеющихсся на сайте тайтлов """

    model = Anime
    template_name = 'anime/all_anime_page.html'
    context_object_name = 'anime'

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


class GenrePageView(ListView):
    ''' вывод страницы со списком всех имеющихся на сайте жанров аниме '''

    model = Genre
    template_name = 'anime/genre_page.html'
    context_object_name = 'genre'

    extra_context = {
        'title': 'Жанры',
        'menu': menu,
    }


class AnimeFromGenrePageView(ListView):
    ''' на страницу выводятся все аниме, соответствующие выбранному жанру '''

    model = Anime
    template_name = 'anime/anime_from_genre_page.html'
    context_object_name = 'anime'

    extra_context = {
        'menu': menu,
    }

    def get_queryset(self):
        self.genre = get_object_or_404(Genre, genre_slug=self.kwargs['genre_slug'])
        return Anime.objects.filter(genre=self.genre)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = (self.genre.name).capitalize()
        return context


class YearsPageView(ListView):
    ''' вывод страницы со списком всех имеющихся на сайте годами выпуска аниме '''

    model = Years
    template_name = 'anime/year_page.html'
    context_object_name = 'years'

    extra_context = {
        'title': 'Все года',
        'menu': menu,
    }


class AnimeFromYearPageView(ListView):
    ''' на страницу выводятся все аниме, соответствующие выбранному году  '''

    model = Anime
    template_name = 'anime/anime_year_page.html'
    context_object_name = 'anime'

    extra_context = {
        'menu': menu,
    }

    def get_queryset(self):
        year = get_object_or_404(Years, years=self.kwargs['year'])
        return Anime.objects.filter(year=year)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.kwargs['year']
        return context


class AnimeFromProducerPageView(ListView):
    ''' на страницу выводятся все аниме, соответствующие выбранному режиссеру '''

    model = Anime
    template_name = 'anime/producer_page.html'
    context_object_name = 'anime'

    extra_context = {
        'menu': menu,
    }

    def get_queryset(self):
        producer = get_object_or_404(Producer, producer_slug=self.kwargs['producer_slug'])
        return Anime.objects.filter(producer=producer)


class AnimeFromAuthorPageView(ListView):
    ''' на страницу выводятся все аниме, соответствующие выбранному автору оригинала '''

    model = Anime
    template_name = 'anime/author_page.html'
    context_object_name = 'anime'

    extra_context = {
        'menu': menu,
    }

    def get_queryset(self):
        author = get_object_or_404(Author, author_slug=self.kwargs['author_slug'])
        return Anime.objects.filter(author=author)


class AnimeFromTagPageView(ListView):
    ''' на страницу выводятся все аниме, соответствующие выбранному тегу '''

    model = Anime
    template_name = 'anime/tag_page.html'
    context_object_name = 'anime'

    extra_context = {
        'menu': menu,
    }

    def get_queryset(self):
        tag = get_object_or_404(Tag, tag_slug=self.kwargs['tag_slug'])
        return Anime.objects.filter(tag=tag)


class StudioPageView(ListView):
    ''' страница со списком студий, которые выпускали те или иные аниме '''

    model = Studio
    template_name = 'anime/anime_studio.html'
    context_object_name = 'studio'

    extra_context = {
        'title': 'Студии',
        'menu': menu,
    }


class AnimeFromStudioPageView(ListView):
    ''' на страницу выводятся все аниме, соответствующие выбранной студии '''

    model = Anime
    template_name = 'anime/studio_page.html'
    context_object_name = 'anime'

    extra_context = {
        'menu': menu,
    }

    def get_queryset(self):
        studio = get_object_or_404(Studio, studio_slug=self.kwargs['studio_slug'])
        return Anime.objects.filter(studio=studio)


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
