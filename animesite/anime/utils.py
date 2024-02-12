menu = [
    {'title': 'Каталог аниме', 'url_name': 'all_anime_page'},
    {'title': 'Поиск по году', 'url_name': 'year_page'},
    {'title': 'Поиск по жанру', 'url_name': 'genre_page'},
    {'title': 'Поиск по студии', 'url_name': 'studio_page'},
    {'title': 'Добавить аниме', 'url_name': 'add_new_anime'},
]


class DataMixin:
    def get_mixin_context(self, context, **kwargs):
        context['menu'] = menu
        context.update(kwargs)
        return context
