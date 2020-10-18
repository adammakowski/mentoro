from django import forms
from .models import Mentor
from pyuploadcare.dj.forms import ImageField, FileField

class MentorForm(forms.ModelForm):
    image_preview = ImageField(label='Wybierz zdjęcie')
    video_presentation = FileField(label='Wybierz wideo')

    class Meta:
        model = Mentor
        fields = ('title', 'category', 'language', 'price', 'who_am_i', 'what_can_i_teach_you', 'description', 'requirements', 'image_preview', 'video_presentation', 'status')
