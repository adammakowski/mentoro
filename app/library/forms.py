from django import forms
from .models import Library

class LibraryForm(forms.ModelForm):

    class Meta:
        model = Library
        fields = ('title', 'price', 'image_preview', 'image_preview', 'short_description', 'description',)