from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Wymagany. Podaj prawidłowy adres e-mail.')
    captcha = ReCaptchaField(required=True, widget=ReCaptchaV2Checkbox, help_text='Potrzebujemy weryfikacji że jesteś człowiekiem.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'captcha']
