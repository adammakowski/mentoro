from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(required=True, help_text='Wpisz własną nazwę użytkownika. Nazwa użytkownika będzie używana przez Ciebie do logowania się na Twoje konto.')
    first_name = forms.CharField(required=None, help_text='Twoje imię posłuży Nam do kontaktu z Tobą.')
    email = forms.EmailField(required=True, help_text='Adres e-mail będzie wykorzystywany do skontaktowania się z Tobą i operacji na Twoim koncie. Nie podzielimy się nim z nikim innym.')
    captcha = ReCaptchaField(required=True, widget=ReCaptchaV2Checkbox, help_text='Prosimy o wykonanie testu na to że nie jesteś robotem.')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'captcha']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
