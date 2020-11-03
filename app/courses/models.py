from django.db import models
from django.utils import timezone
from pyuploadcare.dj.models import ImageField, FileField
from ckeditor.fields import RichTextField


class Category(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['title']

    def __str__(self):
        return self.title


class Language(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)

    def __str__(self):
        return self.title


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Course(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False, null=False, verbose_name='Tytuł', help_text='Wpisz tytuł Twojego wideo kursu')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Kategoria', help_text='Wybierz kategorię w której chcesz dodać kurs')
    language = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name='Język', help_text='Wybierz język w którym są Twoje treści')
    price = models.DecimalField(null=False, blank=False, max_digits=7, decimal_places=2, default='49.99', verbose_name='Cena', help_text='Podaj cenę w złotówkach za która chcesz sprzedawać materiał')
    short_description = RichTextField(blank=False, null=False, verbose_name='Krótki opis', help_text='Dodaj krótki opis. Maksymalna ilość znaków to 500')
    description = RichTextField(blank=False, null=False, verbose_name='Szczegółowy opis', help_text='Podaj szczegółowy opis Twojego materiału.')
    contests = RichTextField(blank=False, null=False, default='', verbose_name="Zawartość i spis treści", help_text='Podaj zawartość i spis treści Twojego materiału')
    requirements = RichTextField(blank=False, null=False, default='', verbose_name="Wymagana wiedza", help_text='Wymagana wiedza do zrozumienia materiału')
    image_preview = ImageField(blank=False, null=False, verbose_name='Zdjęcie podglądowe', help_text='Dodaj zdjęcie podglądowe kursu')
    video_preview = FileField(blank=False, null=False, verbose_name='Wideo prezentacja', help_text='Dodaj film wideo reklamujący i prezentująćy Twoj wideo kurs')
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        ordering = ['-created_date']

    def __str__(self):
        return self.title


class Lesson(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Kurs do którego dodajesz lekcje', help_text='Dodaj lekcje')
    position = models.IntegerField()
    free_lesson = models.BooleanField(default=False)
    title = models.CharField(max_length=200, blank=False, null=False)
    description = RichTextField(blank=False, null=False)
    video = FileField(blank=False, null=False)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = "Lesson"
        verbose_name_plural = "Lessons"
        ordering = ['-position']

    def __str__(self):
        return self.title
