from django.urls import path

from . import views

urlpatterns = [
    path('', views.AnimeHomePage.as_view(), name='index'),
    path('anime/', views.AllAnimePage.as_view(), name='all_anime'),
    path('anime/<slug:anime_slug>', views.show_anime_page, name='anime_page'),
    path('anime/genre/', views.GenrePage.as_view(), name='anime_genre'),
    path('anime/genre/<slug:genre_slug>', views.AnimeFromGenrePage.as_view(), name='genre_page'),
    path('anime/year/', views.YearsPage.as_view(), name='anime_years'),
    path('anime/year/<int:year>', views.AnimeFromYearPage.as_view(), name='year_page'),
    path('anime/producer/<slug:producer_slug>', views.show_producer_page, name='producer_page'),
    path('anime/author/<slug:author_slug>', views.show_author_page, name='author_page'),
    path('anime/tag/<slug:tag_slug>', views.show_tag_page, name='tag_page'),
    path('anime/studio/', views.StudioPage.as_view(), name='anime_studio'),
    path('anime/studio/<slug:studio_slug>', views.show_studio_page, name='studio_page'),
    path('anime/add/', views.addanime, name='addanime'),
]