from django import forms
from .models import Course
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, Column, Field

class CourseForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'title',
            'category',
            'language',
            'price',
            'short_description',
            'description',
            Div('image_preview', css_class=""),
            Div('video_preview', css_class="course_create_pond"),
            Submit('submit', 'Dodaj kurs', css_class='btn btn-success btn-block shadow rounded-0 font-weight-bold')
        )

    class Meta:
        model = Course
        fields = ('title', 'price', 'category', 'language', 'short_description', 'description', 'image_preview', 'video_preview',)