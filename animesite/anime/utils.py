menu = [
    {'title': 'Каталог аниме', 'url_name': 'all_anime_page'},
    {'title': 'Поиск по году', 'url_name': 'year_page'},
    {'title': 'Поиск по жанру', 'url_name': 'genre_page'},
    {'title': 'Поиск по студии', 'url_name': 'studio_page'},
    {'title': 'Добавить аниме', 'url_name': 'add_new_anime'},
]


class DataMixin:
    title_page = None
    extra_context = {}

    def __init__(self):
        if self.title_page:
            self.extra_context['title'] = self.title_page

        if 'menu' not in self.extra_context:
            self.extra_context['menu'] = menu

    def get_mixin_context(self, context, **kwargs):
        context['menu'] = menu
        context.update(kwargs)
        return context
