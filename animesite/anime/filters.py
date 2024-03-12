from django_filters import FilterSet

from anime.models import Anime


class AnimeFilter(FilterSet):
    class Meta:
        model = Anime
        fields = {
            'name_ru': ['icontains'],
            'name_en': ['icontains'],
            'name_jp': ['icontains'],
        }
