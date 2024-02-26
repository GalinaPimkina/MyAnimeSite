from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django import forms


class LoginUserForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class RegistrationUserForm(UserCreationForm):
    ''' форма регистрации нового пользователя '''

    username = forms.CharField(label="Логин")
    password1 = forms.CharField(label="Пароль")
    password2 = forms.CharField(label="Повтор пароля")

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        labels = {
            'email': 'E-mail',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такой e-mail уже используется!")
        return email


class ProfileUserForm(forms.ModelForm):
    ''' форма отображения профиля пользователя '''

    username = forms.CharField(disabled=True, label="Логин")
    email = forms.CharField(disabled=True, label="E-mail")

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }


class UserPasswordChangeForm(PasswordChangeForm):
    ''' форма для смены пароля пользователя '''

    old_password = forms.CharField(label="Старый пароль")
    new_password1 = forms.CharField(label="Новый пароль")
    new_password2 = forms.CharField(label="Повтор пароля")
