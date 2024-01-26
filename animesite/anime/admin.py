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

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', ]

@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    list_display = ['name', ]

@admin.register(Studio)
class StudioAdmin(admin.ModelAdmin):
    list_display = ['name', ]


admin.site.register(Tag)
admin.site.register(Character)
admin.site.register(Seiyuu)