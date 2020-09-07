from django import forms
from .models import Mentor
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, HTML

class MentorForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'title',
            'category',
            'language',
            'price',
            'who_am_i',
            'what_can_i_teach_you',
            'description',
            'requirements',
            Div('image_preview', css_class=""),
            Div('video_presentation', css_class=""),
            'status',
            Submit('submit', 'Zgłoś kandydaturę', css_class='btn btn-success btn-block shadow rounded-0 font-special-bold'),
        )

    class Meta:
        model = Mentor
        fields = ('title', 'category', 'language', 'price', 'who_am_i', 'what_can_i_teach_you', 'description', 'requirements', 'image_preview', 'video_presentation', 'status')