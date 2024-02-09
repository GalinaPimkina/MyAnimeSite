from django.urls import path

from . import views

urlpatterns = [
    path('', views.AnimeHomePageView.as_view(), name='anime_home_page'),
    path('anime/', views.AllAnimePageView.as_view(), name='all_anime_page'),
    path('anime/<slug:anime_slug>', views.AnimePageView.as_view(), name='anime_page'),
    path('anime/genre/', views.GenrePageView.as_view(), name='genre_page'),
    path('anime/genre/<slug:genre_slug>', views.AnimeFromGenrePageView.as_view(), name='anime_from_genre_page'),
    path('anime/year/', views.YearsPageView.as_view(), name='year_page'),
    path('anime/year/<int:year>', views.AnimeFromYearPageView.as_view(), name='anime_from_year_page'),
    path('anime/producer/<slug:producer_slug>', views.AnimeFromProducerPageView.as_view(), name='anime_from_producer_page'),
    path('anime/author/<slug:author_slug>', views.AnimeFromAuthorPageView.as_view(), name='anime_from_author_page'),
    path('anime/tag/<slug:tag_slug>', views.AnimeFromTagPageView.as_view(), name='anime_from_tag_page'),
    path('anime/studio/', views.StudioPageView.as_view(), name='studio_page'),
    path('anime/studio/<slug:studio_slug>', views.AnimeFromStudioPageView.as_view(), name='anime_from_studio_page'),
    path('anime/addanime/', views.AddNewAnime.as_view(), name='add_new_anime'),
    path('anime/addgenre/', views.AddNewGenre.as_view(), name='add_new_genre'),
    path('anime/addyear/', views.AddNewYear.as_view(), name='add_new_year'),
    path('anime/addproducer/', views.AddNewProducer.as_view(), name='add_new_producer'),
    path('anime/addauthor/', views.AddNewAuthor.as_view(), name='add_new_author'),
    path('anime/addtag/', views.AddNewTag.as_view(), name='add_new_tag'),
    path('anime/addstudio/', views.AddNewStudio.as_view(), name='add_new_studio'),
]