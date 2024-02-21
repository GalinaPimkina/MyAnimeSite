from django.contrib.auth.views import LoginView
from django.shortcuts import render

from users.forms import LoginUserForm, RegistrationUserForm


class LoginUserView(LoginView):
    ''' авторизация '''
    form_class = LoginUserForm
    template_name = 'users/login_user.html'
    extra_context = {'title': 'Авторизация'}


def registration(request):
    ''' регистрация '''
    form = RegistrationUserForm()
    return render(request, 'users/registration.html', {'form':form})