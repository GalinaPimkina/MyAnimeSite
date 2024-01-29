from django.contrib import admin

from anime.models import Anime, Genre, Years, Author, Producer, Studio, Tag, Character, Seiyuu, AnimeGenreTable, \
    AnimeTagTable, AnimeProducerTable


class AnimeGenreInline(admin.TabularInline):
    model = AnimeGenreTable
    extra = 1
    verbose_name = "Жанр"
    verbose_name_plural = "Жанры"

class AnimeTagInline(admin.TabularInline):
    model = AnimeTagTable
    extra = 1

class AnimeProducerInline(admin.TabularInline):
    model = AnimeProducerTable
    extra = 1

@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    inlines = (AnimeGenreInline, AnimeTagInline, AnimeProducerInline, )
    list_display = ['name_ru', 'year', 'studio', 'brief_info']
    list_per_page = 5
    ordering = ['year', 'studio', 'name_ru']
    search_fields = ['name_ru', 'studio__name']

    @admin.display(description="Краткое описание")
    def brief_info(self, anime: Anime):
        return f"Описание {len(anime.description)} символов."


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    inlines = (AnimeGenreInline, )
    list_display = ['name', 'genre_slug']
    search_fields = ['name']

@admin.register(Years)
class YearsAdmin(admin.ModelAdmin):
    list_display = ['years', ]
    search_fields = ['years']

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