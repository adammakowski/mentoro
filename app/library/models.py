from django.db import models
from optimized_image.fields import OptimizedImageField
from simple_history.models import HistoricalRecords
from ckeditor.fields import RichTextField

STATUS = (
    (0, "Draft"),
    (1, "Publish")
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


class Library(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=150, unique=True, blank=False, null=False, verbose_name="Tytuł", help_text='Podaj tytuł wpisu który chcesz dodać')
    slug = models.SlugField(max_length=150, unique=True, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Kategoria", help_text='Wybierz kategorię w której chcesz dodać wpis')
    language = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name="Język", help_text='Wybierz język w którym są Twoje treści')
    price = models.DecimalField(null=False, blank=False, max_digits=7, decimal_places=2, verbose_name="Cena", help_text="Podaj cenę w złotówkach za która chcesz sprzedawać materiał")
    short_description = RichTextField(blank=False, null=False, max_length=500, verbose_name="Krótki opis", help_text='Dodaj krótki opis. Maksymalna ilość znaków to 500')
    description = RichTextField(blank=False, null=False, verbose_name="Szczegółowy opis", help_text='Podaj szczegółowy opis Twojego materiału.')
    contests = RichTextField(blank=False, null=False, verbose_name="Zawartość i spis treści", help_text='Podaj zawartość i spis treści Twojego materiału')
    requirements = RichTextField(blank=False, null=False, verbose_name="Wymagana wiedza", help_text='Wymagana wiedza do zrozumienia materiału')
    image_preview = OptimizedImageField(upload_to='library/image_library_preview/%Y/%m/%d/', blank=False, null=False, verbose_name="Zdjęcie podglądowe", help_text='Dodaj zdjęcie podglądowe materiału')
    video_preview = models.FileField(upload_to='library/video_library_preview/%Y/%m/%d/', blank=True, null=True, verbose_name="Wideo prezentacja", help_text='Dodaj film wideo reklamujący i opisujący Twoj materiał')
    file_download = models.FileField(upload_to='library/files_library/%Y/%m/%d/', blank=False, null=False, verbose_name="Plik do pobrania", help_text='Dodaj plik który kupujący będzie mógł pobrać. Dozwolone formaty to: zip, rar, pdf, txt, epub')
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    history = HistoricalRecords()

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Library, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='comments')
    body = RichTextField(blank=False, null=False, verbose_name="Treść komentarza", help_text='Napisz szczegółowy komentarz. Wesprzyj Twórcę tego postu i przekaż swoje podziękowania lub uwagi.')
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.author)
