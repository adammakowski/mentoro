from django import forms
from .models import Library, Comment

class LibraryForm(forms.ModelForm):

    class Meta:
        model = Library
        fields = ('title', 'category', 'language', 'price', 'short_description', 'description', 'contests', 'requirements', 'image_preview', 'video_preview', 'file_download',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
