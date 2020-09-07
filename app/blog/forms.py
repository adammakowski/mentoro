from django import forms
from .models import Post, Comment

class BlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'language', 'short_description', 'description', 'image_preview',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
