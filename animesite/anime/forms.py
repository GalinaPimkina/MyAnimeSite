from django import forms

from anime.models import Anime


class AddAnimeForm(forms.ModelForm):
    class Meta:
        model = Anime
        fields = ['name_ru', 'name_en', 'name_jp', 'genre', 'episodes', 'year', 'producer', 'author', 'tag', 'studio', 'description']