from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import AddAnimeForm, AddNewGenreForm, AddNewYearForm, AddNewProducerForm, AddNewAuthorForm, AddNewTagForm, \
    AddNewStudioForm
from .models import Anime, Genre, Producer, Tag, Years, Author, Studio
from .utils import DataMixin


class AnimeHomePageView(DataMixin, ListView):
    '''главная страница сайта, выводится список всех аниме/
    пока что практически аналог AllAnimePage, но будет изменена в дальнейшем'''

    model = Anime
    template_name = 'anime/anime_home_page.html'
    context_object_name = 'anime'
    title_page = 'Главная страница'


class AllAnimePageView(DataMixin, ListView):
    """ страница отображения всех имеющихсся на сайте тайтлов """

    model = Anime
    template_name = 'anime/all_anime_page.html'
    context_object_name = 'anime'
    title_page = 'Каталог аниме'


class AnimePageView(DataMixin, DetailView):
    ''' страница с описанием одного конкретного аниме '''

    model = Anime
    template_name = 'anime/anime_page.html'
    slug_url_kwarg = 'anime_slug'
    context_object_name = 'anime'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context,
                                      title=context['anime'].name_ru,
                                      genre=Genre.objects.filter(genre__slug=self.kwargs[self.slug_url_kwarg]),
                                      producer=Producer.objects.filter(producer__slug=self.kwargs[self.slug_url_kwarg]),
                                      tag=Tag.objects.filter(tags__slug=self.kwargs[self.slug_url_kwarg]),
                                      studio=Studio.objects.filter(studio__slug=self.kwargs[self.slug_url_kwarg]))


class GenrePageView(DataMixin, ListView):
    ''' вывод страницы со списком всех имеющихся на сайте жанров аниме '''

    model = Genre
    template_name = 'anime/genre_page.html'
    context_object_name = 'genre'
    title_page = 'Поиск по жанру'


class AnimeFromGenrePageView(DataMixin, ListView):
    ''' на страницу выводятся все аниме, соответствующие выбранному жанру '''

    model = Anime
    template_name = 'anime/anime_from_genre_page.html'
    context_object_name = 'anime'

    def get_queryset(self):
        self.genre = get_object_or_404(Genre, genre_slug=self.kwargs['genre_slug'])
        return Anime.objects.filter(genre=self.genre)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=f'Поиск по жанру: {self.genre.name}')


class YearsPageView(DataMixin, ListView):
    ''' вывод страницы со списком всех имеющихся на сайте годами выпуска аниме '''

    model = Years
    template_name = 'anime/year_page.html'
    context_object_name = 'years'
    title_page = 'Поиск по году'


class AnimeFromYearPageView(DataMixin, ListView):
    ''' на страницу выводятся все аниме, соответствующие выбранному году  '''

    model = Anime
    template_name = 'anime/anime_from_year_page.html'
    context_object_name = 'anime'

    def get_queryset(self):
        self.year = get_object_or_404(Years, years=self.kwargs['year'])
        return Anime.objects.filter(year=self.year)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=f'Поиск по году: {self.year}')


class AnimeFromProducerPageView(DataMixin, ListView):
    ''' на страницу выводятся все аниме, соответствующие выбранному режиссеру '''

    model = Anime
    template_name = 'anime/anime_from_producer_page.html'
    context_object_name = 'anime'

    def get_queryset(self):
        self.producer = get_object_or_404(Producer, producer_slug=self.kwargs['producer_slug'])
        return Anime.objects.filter(producer=self.producer)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=f'Поиск по режиссеру: {self.producer.name}')


class AnimeFromAuthorPageView(DataMixin, ListView):
    ''' на страницу выводятся все аниме, соответствующие выбранному автору оригинала '''

    model = Anime
    template_name = 'anime/anime_from_author_page.html'
    context_object_name = 'anime'
    

    def get_queryset(self):
        self.author = get_object_or_404(Author, author_slug=self.kwargs['author_slug'])
        return Anime.objects.filter(author=self.author)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=f'Поиск по автору оригинала: {self.author.name}')


class AnimeFromTagPageView(DataMixin, ListView):
    ''' на страницу выводятся все аниме, соответствующие выбранному тегу '''

    model = Anime
    template_name = 'anime/anime_from_tag_page.html'
    context_object_name = 'anime'

    def get_queryset(self):
        self.tag = get_object_or_404(Tag, tag_slug=self.kwargs['tag_slug'])
        return Anime.objects.filter(tag=self.tag)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=f'Поиск по тегу: {self.tag.tag}')


class StudioPageView(DataMixin, ListView):
    ''' страница со списком студий, которые выпускали те или иные аниме '''

    model = Studio
    template_name = 'anime/studio_page.html'
    context_object_name = 'studio'
    title_page = 'Поиск по студии'


class AnimeFromStudioPageView(DataMixin, ListView):
    ''' на страницу выводятся все аниме, соответствующие выбранной студии '''

    model = Anime
    template_name = 'anime/anime_from_studio_page.html'
    context_object_name = 'anime'

    def get_queryset(self):
        self.studio = get_object_or_404(Studio, studio_slug=self.kwargs['studio_slug'])
        return Anime.objects.filter(studio=self.studio)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=f'Поиск по студии: {self.studio.name}')


class AddNewAnimeView(DataMixin, CreateView):
    ''' добавляет новое аниме на сайт '''

    form_class = AddAnimeForm
    template_name = 'anime/add_new_anime.html'
    title_page = 'Добавить аниме'


class AddNewGenreView(DataMixin, CreateView):
    ''' позволяет добавить новый жанр, если его еще нет '''

    form_class = AddNewGenreForm
    template_name = 'anime/add_new_genre.html'
    title_page = 'Добавить жанр'


class AddNewYearView(DataMixin, CreateView):
    ''' позволяет добавить год, если его еще нет '''

    form_class =  AddNewYearForm
    template_name = 'anime/add_new_year.html'
    title_page = 'Добавить год'


class AddNewProducerView(DataMixin, CreateView):
    ''' позволяет добавить режиссера, если его еще нет '''

    form_class = AddNewProducerForm
    template_name = 'anime/add_new_producer.html'
    title_page = 'Добавить режиссера'


class AddNewAuthorView(DataMixin, CreateView):
    ''' позволяет добавить автора оригинала, если его еще нет '''

    form_class = AddNewAuthorForm
    template_name = 'anime/add_new_author.html'
    title_page = 'Добавить автора оригинала'


class AddNewTagView(DataMixin, CreateView):
    ''' позволяет добавить тег, если его еще нет '''

    form_class = AddNewTagForm
    template_name = 'anime/add_new_tag.html'
    title_page = 'Добавить тег'


class AddNewStudioView(DataMixin, CreateView):
    ''' позволяет добавить студию, если ее еще нет '''

    form_class = AddNewStudioForm
    template_name = 'anime/add_new_studio.html'
    title_page = 'Добавить студию'


class EditAnimeView(DataMixin, UpdateView):
    ''' редактирование аниме '''

    model = Anime
    fields = ['name_ru', 'name_en', 'name_jp', 'genre', 'episodes', 'year', 'producer', 'author', 'tag', 'studio', 'description']
    template_name = 'anime/add_new_anime.html'
    title_page = 'Редактировать аниме'


class EditGenreView(DataMixin, UpdateView):
    ''' редактирование жанра '''

    model = Genre
    fields = ['name', ]
    template_name = 'anime/add_new_genre.html'
    title_page = 'Редактировать жанр'
    slug_url_kwarg = 'genre_slug'
    slug_field = 'genre_slug'
