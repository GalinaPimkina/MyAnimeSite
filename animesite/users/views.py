from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from animesite import settings
from users.forms import LoginUserForm, RegistrationUserForm, ProfileUserForm, UserPasswordChangeForm


class LoginUserView(LoginView):
    ''' авторизация '''
    form_class = LoginUserForm
    template_name = 'users/login_user.html'
    extra_context = {'title': 'Авторизация'}


class RegistrationUserView(CreateView):
    ''' регистрация '''
    form_class = RegistrationUserForm
    template_name = 'users/registration.html'
    extra_context = {'title': 'Регистрация'}
    success_url = reverse_lazy('users:registration_success')


def registration_success(request):
    ''' что увидит пользователь после успешной регистрации '''
    return render(request, 'users/registration_success.html')


class UserProfile(LoginRequiredMixin, UpdateView):
    '''отображение страницы с профилем пользователя'''

    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'users/user_profile.html'
    extra_context = {
        'title': 'Профиль пользователя',
        'default_image': settings.DEFAULT_USER_IMAGE,
    }

    def get_success_url(self):
        return reverse_lazy('users:user_profile')

    def get_object(self, queryset=None):
        return self.request.user


class UserPasswordChangeView(PasswordChangeView):
    '''класс для смены пароля пользователя.
    унаследован от базового PasswordChangeView,
    изменена только ссылка переадресации success_url,
     т.к. требуется дополнительно указать пространство имен users '''

    form_class = UserPasswordChangeForm
    success_url = reverse_lazy('users:password_change_done')
    template_name = 'users/password_change.html'