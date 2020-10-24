from django.db import models
from django.utils import timezone
from pyuploadcare.dj.models import ImageField, FileField
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Public(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(default='', max_length=100, blank=False, null=False, verbose_name='Imię')
    last_name = models.CharField(default='', max_length=100, blank=False, null=False, verbose_name='Nazwisko')
    avatar = ImageField(blank=False, null=False, verbose_name='Zdjęcie profilowe')
    banner = ImageField(blank=True, null=True, verbose_name='Zdjęcie w tle')
    video = FileField(blank=True, null=True, verbose_name='Wideo prezentacja')
    bio = RichTextField(blank=True, null=True, verbose_name='Biografia')
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    youtube = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    behance = models.URLField(null=True, blank=True)
    dribbble = models.URLField(null=True, blank=True)
    flickr = models.URLField(null=True, blank=True)
    tumblr = models.URLField(null=True, blank=True)
    vimeo = models.URLField(null=True, blank=True)
    deviantart = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    bitbucket = models.URLField(null=True, blank=True)
    verification = models.BooleanField(default=False, verbose_name='Weryfikacja profilu')
    active = models.BooleanField(default=False, verbose_name='Zatwierdzone')

    def __str__(self):
        return self.first_name