from django.shortcuts import render
from django.views.generic import ListView

from anime.utils import DataMixin
from news.models import Post


class HomePageView(DataMixin, ListView):
    '''главная страница сайта, выводится список новостей '''

    model = Post
    template_name = 'news/index.html'
    context_object_name = 'post'
    title_page = 'Главная страница'