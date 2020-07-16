from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(required=True, help_text='Wpisz Twoją nazwę użytkownika. Nazwa użytkownika zostanie użyta do zalogowania się na twoje konto.')
    email = forms.EmailField(required=True, help_text='Adres e-mail zostanie wykorzystany do skontaktowania się z Tobą i operacji na koncie. Nie podzielimy się nim z nikim innym.')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
