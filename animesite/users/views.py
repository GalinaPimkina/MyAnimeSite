from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from users.forms import LoginUserForm


class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login_user.html'
    extra_context = {'title': 'Авторизация'}
