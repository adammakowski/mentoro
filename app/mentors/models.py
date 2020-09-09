from django.db import models
from django.utils import timezone
from optimized_image.fields import OptimizedImageField
from simple_history.models import HistoricalRecords
from ckeditor.fields import RichTextField

STATUS = (
    (0,"Szkic"),
    (1,"Gotowe")
)

class Category(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    history = HistoricalRecords()

    def __str__(self):
        return self.title

class Language(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    history = HistoricalRecords()

    def __str__(self):
        return self.title

class Mentor(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=150, blank=False, null=False, verbose_name='Tytuł', help_text='Tytuł to coś bardzo ważnego, zastanów się nad nim dobrze')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Kategoria", help_text='Wybierz kategorię w której nauczasz', default=Category)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name="Język", help_text='Wybierz język w którym nauczasz', default=Language)
    price = models.DecimalField(null=False, blank=False, max_digits=7, decimal_places=2, default='50', verbose_name='Cena', help_text='Ustal cenę która będziesz pobierać miesiecznie za nauczanie od każdego ucznia')
    who_am_i = RichTextField(blank=False, null=False, verbose_name='Kim jestem?', help_text='Napisz jak najwięcej o sobie, kim jesteś, czego nauczasz i w jaki sposób')
    description = RichTextField(blank=False, null=False, verbose_name='Szczegółowy opis i dodatkowe informacje', help_text='Czym więcej informacji dla potencjalnego ucznia tym lepiej, napisz jak najwięcej.')
    what_can_i_teach_you = RichTextField(blank=False, null=False, verbose_name='Czego mogę nauczyć')
    requirements = RichTextField(blank=False, null=False, verbose_name='Moje wymagania od ucznia')
    image_preview = OptimizedImageField(upload_to='mentors/image_preview/%Y/%m/%d/', blank=False, null=False, verbose_name='Zdjęcie podglądowe')
    video_presentation = models.FileField(upload_to='mentors/video_presentation/%Y/%m/%d/', blank=True, null=True, verbose_name='Wideo prezentacja')
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0, help_text='Status publikacji')
    active = models.BooleanField(default=False, verbose_name='Zatwierdzone')
    history = HistoricalRecords()

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title