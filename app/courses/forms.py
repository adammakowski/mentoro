from django import forms
from .models import Course

class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ('title', 'price', 'image_preview', 'video_preview', 'short_description', 'description',)