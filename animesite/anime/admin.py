from django.contrib import admin

from anime.models import Anime, Genre, Years, Author

admin.site.register(Anime)
admin.site.register(Genre)
admin.site.register(Years)
admin.site.register(Author)