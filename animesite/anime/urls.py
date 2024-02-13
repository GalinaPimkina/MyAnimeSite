from django.urls import path

from . import views

urlpatterns = [
    path('', views.AnimeHomePageView.as_view(), name='anime_home_page'),
    path('anime/', views.AllAnimePageView.as_view(), name='all_anime_page'),
    path('anime/add/', views.AddNewAnimeView.as_view(), name='add_new_anime'),
    path('anime/edit/<slug:anime_slug>/', views.EditAnimeView.as_view(), name='edit_anime'),
    path('anime/<slug:anime_slug>/', views.AnimePageView.as_view(), name='anime_page'),
    path('genre/', views.GenrePageView.as_view(), name='genre_page'),
    path('genre/add/', views.AddNewGenreView.as_view(), name='add_new_genre'),
    path('genre/edit/<slug:genre_slug>/', views.EditGenreView.as_view(), name='edit_genre'),
    path('genre/<slug:genre_slug>/', views.AnimeFromGenrePageView.as_view(), name='anime_from_genre_page'),
    path('year/', views.YearsPageView.as_view(), name='year_page'),
    path('year/add/', views.AddNewYearView.as_view(), name='add_new_year'),
    path('year/edit/<slug:year>/', views.EditYearView.as_view(), name='edit_year'),
    path('year/<int:year>/', views.AnimeFromYearPageView.as_view(), name='anime_from_year_page'),
    path('producer/add/', views.AddNewProducerView.as_view(), name='add_new_producer'),
    path('producer/edit/<slug:producer_slug>/', views.EditProducerView.as_view(), name='edit_producer'),
    path('producer/<slug:producer_slug>/', views.AnimeFromProducerPageView.as_view(), name='anime_from_producer_page'),
    path('author/add/', views.AddNewAuthorView.as_view(), name='add_new_author'),
    path('author/edit/<slug:author_slug>/', views.EditAuthorView.as_view(), name='edit_author'),
    path('author/<slug:author_slug>/', views.AnimeFromAuthorPageView.as_view(), name='anime_from_author_page'),
    path('tag/add/', views.AddNewTagView.as_view(), name='add_new_tag'),
    path('tag/<slug:tag_slug>/', views.AnimeFromTagPageView.as_view(), name='anime_from_tag_page'),
    path('studio/', views.StudioPageView.as_view(), name='studio_page'),
    path('studio/add/', views.AddNewStudioView.as_view(), name='add_new_studio'),
    path('studio/edit/<slug:studio_slug>/', views.EditStudioView.as_view(), name='edit_studio'),
    path('studio/<slug:studio_slug>/', views.AnimeFromStudioPageView.as_view(), name='anime_from_studio_page'),
]