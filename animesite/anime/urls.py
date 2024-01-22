from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('anime/', views.show_all_anime, name='all_anime'),
    path('anime/<slug:anime_slug>', views.show_anime_page, name='anime_page'),
    path('anime/genre/', views.anime_genre, name='anime_genre'),
    path('anime/<slug:genre_slug>', views.show_genre_page, name='genre_page'),
    path('anime/year/', views.anime_years, name='anime_years'),
    path('anime/year/<int:year>', views.show_year_page, name='year_page'),
    path('anime/producer/<slug:producer_slug>', views.show_producer_page, name='producer_page'),
    path('anime/author/<slug:author_slug>', views.show_author_page, name='author_page'),
    path('anime/tag/<slug:tag_slug>', views.show_tag_page, name='tag_page'),
    path('anime/studio/', views.anime_studio, name='anime_studio'),
    path('anime/studio/<slug:studio_slug>', views.show_studio_page, name='studio_page'),
]