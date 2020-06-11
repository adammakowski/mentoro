from django import forms
from .models import LibraryFile

class LibraryForm(forms.ModelForm):

    class Meta:
        model = LibraryFile
        fields = ('title', 'category', 'language', 'price', 'short_description', 'description', 'image_preview', 'video_preview', 'file_download',)