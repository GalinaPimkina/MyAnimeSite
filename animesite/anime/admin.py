from django.contrib import admin

from anime.models import Anime, Genre, Years

admin.site.register(Anime)
admin.site.register(Genre)
admin.site.register(Years)