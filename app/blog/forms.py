from django import forms
from .models import Post, Comment

class BlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'language', 'content', 'image_preview', 'status')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
