from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, \
    PasswordResetDoneView
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.LoginUserView.as_view(), name='login_user'),
    path('logout/', LogoutView.as_view(), name='logout_user'),
    path('registration/', views.RegistrationUserView.as_view(), name='registration'),
    path('registration_success/', views.registration_success, name='registration_success'),
    path('user_profile/', views.UserProfile.as_view(), name='user_profile'),
    path('user_profile/password_change/', views.UserPasswordChangeView.as_view(), name='password_change'),
    path('user_profile/password_change/done/', PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password_change_done'),
    path('password_reset/', PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done.html')
]