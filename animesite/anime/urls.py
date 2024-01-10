from django.urls import path

from animesite.anime import views

urlpatterns = [
    path('', views.index, name='index'),
]