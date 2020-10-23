from django.db import models
from pyuploadcare.dj.models import ImageField
from ckeditor.fields import RichTextField

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

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

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=150, unique=True, blank=False, null=False, verbose_name="Tytuł", help_text='Podaj tytuł wpisu który chcesz dodać')
    slug = models.SlugField(max_length=150, unique=True, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Kategoria", help_text='Wybierz kategorię w której chcesz dodać wpis')
    language = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name="Język", help_text='Wybierz język w którym są Twoje treści')
    short_description = RichTextField(blank=False, null=False, max_length=500, verbose_name="Krótki opis", help_text='Dodaj krótki opis. Maksymalna ilość znaków to 500')
    description = RichTextField(blank=False, null=False, verbose_name="Szczegółowy opis", help_text='Podaj szczegółowy opis Twojego materiału.')
    image_preview = ImageField(blank=False, null=False, verbose_name="Zdjęcie podglądowe", help_text='Dodaj zdjęcie podglądowe materiału')
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now= True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-created_date']

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comments')
    name = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = RichTextField(blank=False, null=False, verbose_name="Treść komentarza", help_text='Napisz szczegółowy komentarz. Wesprzyj Twórcę tego postu i przekaż swoje podziękowania lub uwagi.')
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)