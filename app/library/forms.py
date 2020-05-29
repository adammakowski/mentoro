from django import forms
from .models import LibraryFile

class LibraryForm(forms.ModelForm):

    class Meta:
        model = LibraryFile
        fields = ('title', 'price', 'image_preview', 'image_preview', 'short_description', 'description',)