from django.urls import path

from news import views

app_name = 'news'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('post/<slug:post_slug>/', views.PostPageView.as_view(), name='post_page'),
]