from django.contrib import admin

from anime.models import Anime, Genre, Years, Author, Producer, Studio, Tag, Character, Seiyuu



@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ['name_ru', 'year', 'added']
    list_per_page = 5
    ordering = ['year', 'name_ru', 'added']
    search_fields = ['name_ru', 'added']
    filter_horizontal = ['genre', 'tag', 'producer']

    @admin.display(description="Краткое описание")
    def brief_info(self, anime: Anime):
        return f"Описание {len(anime.description)} символов."


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name', 'genre_slug']
    search_fields = ['name']

@admin.register(Years)
class YearsAdmin(admin.ModelAdmin):
    list_display = ['year', ]
    search_fields = ['year']

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ['name']

@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ['name']

@admin.register(Studio)
class StudioAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ['name']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['tag', 'tag_slug', ]
    search_fields = ['tag']

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ['name', 'seiyuu', ]
    search_fields = ['name', 'seiyuu']

@admin.register(Seiyuu)
class SeiyuuAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ['name']