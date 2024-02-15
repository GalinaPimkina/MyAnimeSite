from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

from users.forms import LoginUserForm


def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            user = authenticate(request,
                                username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse_lazy('anime_home_page'))
    else:
        form = LoginUserForm()

    return render(request, 'users/login_user.html', {'form': form})


def logout_user(request):
    return HttpResponse("logout")
