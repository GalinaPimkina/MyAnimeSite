from django.contrib import admin

from anime.models import Anime, Genre, Years, Author, Producer, Studio, Tag, Character, Seiyuu

class AnimeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_ru', 'slug', 'episodes', 'year', ]


admin.site.register(Anime)
admin.site.register(Genre)
admin.site.register(Years)
admin.site.register(Author)
admin.site.register(Producer)
admin.site.register(Studio)
admin.site.register(Tag)
admin.site.register(Character)
admin.site.register(Seiyuu)