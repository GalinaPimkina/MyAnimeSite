from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import LoginUserForm, RegistrationUserForm


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
