from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.LoginUserView.as_view(), name='login_user'),
    path('logout/', LogoutView.as_view(), name='logout_user'),
    path('registration/', views.RegistrationUserView.as_view(), name='registration'),
    path('registration_success/', views.registration_success, name='registration_success'),
    path('user_profile/<int:pk>', views.UserProfile.as_view(), name='user_profile'),
]