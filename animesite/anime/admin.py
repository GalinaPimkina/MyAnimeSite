from django.contrib import admin

from anime.models import Anime, Genre, Years, Author, Producer, Studio, Tag, Character, Seiyuu

@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ['name_ru', 'year', 'studio']

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name', 'genre_slug']

@admin.register(Years)
class YearsAdmin(admin.ModelAdmin):
    list_display = ['years', ]


admin.site.register(Author)
admin.site.register(Producer)
admin.site.register(Studio)
admin.site.register(Tag)
admin.site.register(Character)
admin.site.register(Seiyuu)