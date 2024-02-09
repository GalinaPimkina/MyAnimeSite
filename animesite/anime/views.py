from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView

from .forms import AddAnimeForm, AddNewGenreForm, AddNewYearForm, AddNewProducerForm, AddNewAuthorForm, AddNewTagForm, \
    AddNewStudioForm
from .models import Anime, Genre, Producer, Tag, Years, Author, Studio

menu = [
    {'title': 'Каталог аниме', 'url_name': 'all_anime_page'},
    {'title': 'Поиск по году', 'url_name': 'year_page'},
    {'title': 'Поиск по жанру', 'url_name': 'genre_page'},
    {'title': 'Поиск по студии', 'url_name': 'studio_page'},
    {'title': 'Добавить аниме', 'url_name': 'add_new_anime'},
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


class AnimePageView(DetailView):
    ''' страница с описанием одного конкретного аниме '''

    model = Anime
    template_name = 'anime/anime_page.html'
    slug_url_kwarg = 'anime_slug'
    context_object_name = 'anime'

    extra_context = {
        'menu': menu,
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['anime'].name_ru
        context['genre'] = Genre.objects.filter(genre__slug=self.kwargs[self.slug_url_kwarg])
        context['producer'] = Producer.objects.filter(producer__slug=self.kwargs[self.slug_url_kwarg])
        context['tag'] = Tag.objects.filter(tags__slug=self.kwargs[self.slug_url_kwarg])
        context['studio'] = Studio.objects.filter(studio__slug=self.kwargs[self.slug_url_kwarg])
        return context


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
        context['title'] = f'Поиск по жанру: {self.genre.name}'
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
    template_name = 'anime/anime_from_year_page.html'
    context_object_name = 'anime'

    extra_context = {
        'menu': menu,
    }

    def get_queryset(self):
        self.year = get_object_or_404(Years, years=self.kwargs['year'])
        return Anime.objects.filter(year=self.year)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Поиск по году: {self.year}'
        return context


class AnimeFromProducerPageView(ListView):
    ''' на страницу выводятся все аниме, соответствующие выбранному режиссеру '''

    model = Anime
    template_name = 'anime/anime_from_producer_page.html'
    context_object_name = 'anime'

    extra_context = {
        'menu': menu,
    }

    def get_queryset(self):
        self.producer = get_object_or_404(Producer, producer_slug=self.kwargs['producer_slug'])
        return Anime.objects.filter(producer=self.producer)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Поиск по режиссеру: {self.producer.name}'
        return context


class AnimeFromAuthorPageView(ListView):
    ''' на страницу выводятся все аниме, соответствующие выбранному автору оригинала '''

    model = Anime
    template_name = 'anime/anime_from_author_page.html'
    context_object_name = 'anime'

    extra_context = {
        'menu': menu,
    }

    def get_queryset(self):
        self.author = get_object_or_404(Author, author_slug=self.kwargs['author_slug'])
        return Anime.objects.filter(author=self.author)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Поиск по автору оригинала: {self.author.name}'
        return context


class AnimeFromTagPageView(ListView):
    ''' на страницу выводятся все аниме, соответствующие выбранному тегу '''

    model = Anime
    template_name = 'anime/anime_from_tag_page.html'
    context_object_name = 'anime'

    extra_context = {
        'menu': menu,
    }

    def get_queryset(self):
        self.tag = get_object_or_404(Tag, tag_slug=self.kwargs['tag_slug'])
        return Anime.objects.filter(tag=self.tag)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Поиск по тегу: {self.tag.tag}'
        return context


class StudioPageView(ListView):
    ''' страница со списком студий, которые выпускали те или иные аниме '''

    model = Studio
    template_name = 'anime/studio_page.html'
    context_object_name = 'studio'

    extra_context = {
        'title': 'Студии',
        'menu': menu,
    }


class AnimeFromStudioPageView(ListView):
    ''' на страницу выводятся все аниме, соответствующие выбранной студии '''

    model = Anime
    template_name = 'anime/anime_from_studio_page.html'
    context_object_name = 'anime'

    extra_context = {
        'menu': menu,
    }

    def get_queryset(self):
        self.studio = get_object_or_404(Studio, studio_slug=self.kwargs['studio_slug'])
        return Anime.objects.filter(studio=self.studio)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Поиск по студии: {self.studio.name}'
        return context


class AddNewAnime(CreateView):
    ''' добавляет новое аниме на сайт '''

    form_class = AddAnimeForm
    template_name = 'anime/add_new_anime.html'

    extra_context = {
        'menu': menu,
        'title': 'Добавить аниме',
    }


class AddNewGenre(CreateView):
    ''' позволяет добавить новый жанр, если его еще нет '''

    form_class = AddNewGenreForm
    template_name = 'anime/add_new_genre.html'

    extra_context = {
        'menu': menu,
        'title': 'Добавить жанр',
    }


class AddNewYear(CreateView):
    ''' позволяет добавить год, если его еще нет '''

    form_class =  AddNewYearForm
    template_name = 'anime/add_new_year.html'

    extra_context = {
        'menu': menu,
        'title': 'Добавить год',
    }


class AddNewProducer(CreateView):
    ''' позволяет добавить режиссера, если его еще нет '''

    form_class = AddNewProducerForm
    template_name = 'anime/add_new_producer.html'

    extra_context = {
        'menu': menu,
        'title': 'Добавить режиссера',
    }


class AddNewAuthor(CreateView):
    ''' позволяет добавить автора оригинала, если его еще нет '''

    form_class = AddNewAuthorForm
    template_name = 'anime/add_new_author.html'

    extra_context = {
        'menu': menu,
        'title': 'Добавить автора оригинала',
    }


class AddNewTag(CreateView):
    ''' позволяет добавить тег, если его еще нет '''

    form_class = AddNewTagForm
    template_name = 'anime/add_new_tag.html'

    extra_context = {
        'menu': menu,
        'title': 'Добавить тег',
    }


class AddNewStudio(CreateView):
    ''' позволяет добавить студию, если ее еще нет '''

    form_class = AddNewStudioForm
    template_name = 'anime/add_new_studio.html'

    extra_context = {
        'menu': menu,
        'title': 'Добавить студию',
    }