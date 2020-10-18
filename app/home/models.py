from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone


# Create your models here.
class TermsMentor(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    text = RichTextField(blank=False, null=False)
    published_date = models.DateTimeField(default=timezone.now, blank=False, null=False)

    def __str__(self):
        return self.title
