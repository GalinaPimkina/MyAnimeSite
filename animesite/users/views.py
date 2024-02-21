from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import CreateView

from users.forms import LoginUserForm, RegistrationUserForm


class LoginUserView(LoginView):
    ''' авторизация '''
    form_class = LoginUserForm
    template_name = 'users/login_user.html'
    extra_context = {'title': 'Авторизация'}


class RegistrationUserView(CreateView):
    form_class = RegistrationUserForm
    template_name = 'users/registration.html'
    extra_context = {'title': 'Регистрация'}

# def registration(request):
#     ''' регистрация '''
#     if request.method == "POST":
#         form = RegistrationUserForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             return render(request, 'users/registration_success.html')
#     else:
#         form = RegistrationUserForm()
#     return render(request, 'users/registration.html', {'form': form, 'title': 'Регистрация'})