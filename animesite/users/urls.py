from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path, reverse_lazy
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

    path('password_reset/', PasswordResetView.as_view(
                                            template_name='users/password_reset_form.html',
                                            email_template_name='users/password_reset_email.html',
                                            success_url=reverse_lazy('users:password_reset_done')
                                            ),
                                            name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(
                                            template_name='users/password_reset_done.html'),
                                            name='password_reset_done'),
    path('password_reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
                                            template_name='users/password_reset_confirm.html',
                                            success_url=reverse_lazy('users:password_reset_complete')
                                            ),
                                            name='password_reset_confirm'),
    path('password_reset/complete/', PasswordResetCompleteView.as_view(
                                            template_name='users/password_reset_complete.html'),
                                            name='password_reset_complete'),
]