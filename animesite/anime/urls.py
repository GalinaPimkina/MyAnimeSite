from django.urls import path

from . import views

urlpatterns = [
    path('', views.AnimeHomePageView.as_view(), name='anime_home_page'),
    path('anime/', views.AllAnimePageView.as_view(), name='all_anime'),
    path('anime/<slug:anime_slug>', views.show_anime_page, name='anime_page'),
    path('anime/genre/', views.GenrePageView.as_view(), name='anime_genre'),
    path('anime/genre/<slug:genre_slug>', views.AnimeFromGenrePageView.as_view(), name='genre_page'),
    path('anime/year/', views.YearsPageView.as_view(), name='anime_years'),
    path('anime/year/<int:year>', views.AnimeFromYearPageView.as_view(), name='year_page'),
    path('anime/producer/<slug:producer_slug>', views.AnimeFromProducerPageView.as_view(), name='producer_page'),
    path('anime/author/<slug:author_slug>', views.AnimeFromAuthorPageView.as_view(), name='author_page'),
    path('anime/tag/<slug:tag_slug>', views.AnimeFromTagPageView.as_view(), name='tag_page'),
    path('anime/studio/', views.StudioPageView.as_view(), name='anime_studio'),
    path('anime/studio/<slug:studio_slug>', views.AnimeFromStudioPageView.as_view(), name='studio_page'),
    path('anime/add/', views.addanime, name='addanime'),
]