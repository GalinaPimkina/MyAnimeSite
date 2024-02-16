from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.LoginUserView.as_view(), name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
]