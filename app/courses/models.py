from django.db import models
from django.utils import timezone
from optimized_image.fields import OptimizedImageField
from simple_history.models import HistoricalRecords
from ckeditor.fields import RichTextField

class CourseCategory(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    history = HistoricalRecords()

    def __str__(self):
        return self.title

class CourseLanguage(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    history = HistoricalRecords()

    def __str__(self):
        return self.title

class Course(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False, null=False, verbose_name='Tytuł', help_text='Wpisz tytuł Twojego wideo kursu')
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE, verbose_name='Kategoria', help_text='Wybierz kategorię w której chcesz dodać kurs')
    language = models.ForeignKey(CourseLanguage, on_delete=models.CASCADE, verbose_name='Język', help_text='Wybierz język w którym są Twoje treści')
    price = models.DecimalField(null=False, blank=False, max_digits=7, decimal_places=2, default='49.99', verbose_name='Cena', help_text='Podaj cenę w złotówkach za która chcesz sprzedawać materiał')
    short_description = RichTextField(blank=False, null=False, verbose_name='Krótki opis', help_text='Dodaj krótki opis. Maksymalna ilość znaków to 500')
    description = RichTextField(blank=False, null=False, verbose_name='Szczegółowy opis', help_text='Podaj szczegółowy opis Twojego materiału.')
    contests = RichTextField(blank=False, null=False, default='', verbose_name="Zawartość i spis treści", help_text='Podaj zawartość i spis treści Twojego materiału')
    requirements = RichTextField(blank=False, null=False, default='', verbose_name="Wymagana wiedza", help_text='Wymagana wiedza do zrozumienia materiału')
    image_preview = OptimizedImageField(upload_to='courses/image_course_preview/%Y/%m/%d/', blank=False, null=False, verbose_name='Zdjęcie podglądowe', help_text='Dodaj zdjęcie podglądowe kursu')
    video_preview = models.FileField(upload_to='courses/video_course_preview/%Y/%m/%d/', blank=False, null=False, verbose_name='Wideo prezentacja', help_text='Dodaj film wideo reklamujący i prezentująćy Twoj wideo kurs')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    history = HistoricalRecords()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class CourseLesson(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False, null=False)
    description = RichTextField(blank=False, null=False)
    video = models.FileField(upload_to='courses/lessons/video/%Y/%m/%d/', blank=False, null=False)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.title