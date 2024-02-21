from django.contrib import admin

from anime.models import Anime, Genre, Years, Author, Producer, Studio, Tag, Character, Seiyuu



@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ['name_ru', 'year', 'added']
    list_per_page = 5
    ordering = ['year', 'name_ru', 'added']
    search_fields = ['name_ru', 'added']
    filter_horizontal = ['genre', 'tag', 'producer']

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name', 'genre_slug', 'added']
    search_fields = ['name', 'added']

@admin.register(Years)
class YearsAdmin(admin.ModelAdmin):
    list_display = ['year', 'added']
    search_fields = ['year', 'added']

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'added']
    search_fields = ['name', 'added']

@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    list_display = ['name', 'added']
    search_fields = ['name', 'added']

@admin.register(Studio)
class StudioAdmin(admin.ModelAdmin):
    list_display = ['name', 'added']
    search_fields = ['name', 'added']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['tag', 'tag_slug', 'added']
    search_fields = ['tag', 'added']

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ['name', 'seiyuu', 'added']
    search_fields = ['name', 'seiyuu', 'added']

@admin.register(Seiyuu)
class SeiyuuAdmin(admin.ModelAdmin):
    list_display = ['name', 'added']
    search_fields = ['name', 'added']