from django import forms
from .models import BlogPost

class BlogForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ('title', 'category', 'language', 'short_description', 'description', 'image_preview',)