from django.db import models
from django.utils import timezone
from optimized_image.fields import OptimizedImageField
from simple_history.models import HistoricalRecords
from ckeditor.fields import RichTextField

class BlogCategory(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    history = HistoricalRecords()

    def __str__(self):
        return self.title

class BlogLanguage(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    history = HistoricalRecords()

    def __str__(self):
        return self.title

class BlogPost(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=150, blank=False, null=False, verbose_name="Tytuł", help_text='Podaj tytuł wpisu który chcesz dodać')
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, verbose_name="Kategoria", help_text='Wybierz kategorię w której chcesz dodać wpis')
    language = models.ForeignKey(BlogLanguage, on_delete=models.CASCADE, verbose_name="Język", help_text='Wybierz język w którym są Twoje treści')
    short_description = RichTextField(blank=False, null=False, max_length=500, verbose_name="Krótki opis", help_text='Dodaj krótki opis. Maksymalna ilość znaków to 500')
    description = RichTextField(blank=False, null=False, verbose_name="Szczegółowy opis", help_text='Podaj szczegółowy opis Twojego materiału.')
    image_preview = OptimizedImageField(upload_to='blog/image_blog_preview/%Y/%m/%d/', blank=False, null=False, verbose_name="Zdjęcie podglądowe", help_text='Dodaj zdjęcie podglądowe materiału')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)
    history = HistoricalRecords()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title