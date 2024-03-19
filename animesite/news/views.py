from django.shortcuts import render
from django.views.generic import ListView, DetailView

from anime.utils import DataMixin
from news.models import Post


class HomePageView(DataMixin, ListView):
    '''главная страница сайта, выводится список новостей '''

    model = Post
    template_name = 'news/index.html'
    context_object_name = 'post'
    title_page = 'Главная страница'


class PostPageView(DataMixin, DetailView):
    ''' станица отображения конкретной новости(поста) '''

    model = Post
    template_name = 'news/post_page.html'
    context_object_name = 'post'
    slug_field = 'post_slug'
    slug_url_kwarg = 'post_slug'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return self.get_mixin_context(context, title_page=context['post'].title)