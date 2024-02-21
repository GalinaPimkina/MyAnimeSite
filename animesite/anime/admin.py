from django.contrib import admin

from anime.models import Anime, Genre, Years, Author, Producer, Studio, Tag, Character, Seiyuu



@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ['name_ru', 'year', 'action', 'anime_slug']
    list_per_page = 5
    ordering = ['year', 'name_ru', 'action']
    search_fields = ['name_ru', 'action']
    filter_horizontal = ['genre', 'tag', 'producer']

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name', 'action', 'genre_slug',]
    search_fields = ['name', 'action']

@admin.register(Years)
class YearsAdmin(admin.ModelAdmin):
    list_display = ['year', 'action']
    search_fields = ['year', 'action']

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'action', 'author_slug']
    search_fields = ['name', 'action']

@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    list_display = ['name', 'action', 'producer_slug']
    search_fields = ['name', 'action']

@admin.register(Studio)
class StudioAdmin(admin.ModelAdmin):
    list_display = ['name', 'action', 'studio_slug']
    search_fields = ['name', 'action']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['tag', 'tag_slug', 'action', 'tag_slug']
    search_fields = ['tag', 'action']

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ['name', 'seiyuu', 'action', 'character_slug']
    search_fields = ['name', 'seiyuu', 'action']

@admin.register(Seiyuu)
class SeiyuuAdmin(admin.ModelAdmin):
    list_display = ['name', 'action', 'seiyuu_slug']
    search_fields = ['name', 'action']