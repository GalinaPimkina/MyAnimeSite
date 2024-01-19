from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('anime/', views.show_all_anime, name='all_anime'),
    path('anime/<slug:anime_slug>', views.show_anime_page, name='anime_page'),
    path('anime/genre/', views.anime_genre, name='anime_genre'),
    path('anime/<slug:genre_slug>', views.show_genre_page, name='genre_page'),
]