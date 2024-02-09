from django import forms

from anime.models import Anime, Genre, Years, Producer, Author, Tag, Studio


class AddAnimeForm(forms.ModelForm):
    ''' форма позволяет внести данные, чтобы добавить новое аниме '''

    class Meta:
        model = Anime
        fields = ['name_ru', 'name_en', 'name_jp', 'slug', 'genre', 'episodes', 'year', 'producer', 'author', 'tag', 'studio', 'description']


class AddNewGenreForm(forms.ModelForm):
    ''' форма позволяет внести данные, чтобы добавить новый жанр '''

    class Meta:
        model = Genre
        fields = ['name', 'genre_slug']


class AddNewYearForm(forms.ModelForm):
    ''' форма позволяет внести данные, чтобы добавить новый год '''

    class Meta:
        model = Years
        fields = ['years', ]


class AddNewProducerForm(forms.ModelForm):
    ''' форма позволяет внести данные, чтобы добавить новый режиссера '''

    class Meta:
        model = Producer
        fields = ['name', 'producer_slug']


class AddNewAuthorForm(forms.ModelForm):
    ''' форма позволяет внести данные, чтобы добавить нового автора оригинала '''

    class Meta:
        model = Author
        fields = ['name', 'author_slug']


class AddNewTagForm(forms.ModelForm):
    ''' форма позволяет внести данные, чтобы добавить нового тега '''

    class Meta:
        model = Tag
        fields = ['tag', 'tag_slug']


class AddNewStudio(forms.ModelForm):
    ''' форма позволяет внести данные, чтобы добавить новую студию '''

    class Meta:
        model = Studio
        fields = ['name', 'studio_slug']