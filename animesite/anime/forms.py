from django import forms

from anime.models import Anime, Genre


class AddAnimeForm(forms.ModelForm):
    class Meta:
        model = Anime
        fields = ['name_ru', 'name_en', 'name_jp', 'slug', 'genre', 'episodes', 'year', 'producer', 'author', 'tag', 'studio', 'description']


class AddNewGenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name', 'genre_slug']