from django.db import models
from django.utils import timezone
from optimized_image.fields import OptimizedImageField

class Category(models.Model):
    title = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.title

class Library(models.Model):
    # Choices
    LANGUAGE = (
        ("English", "English"),
        ("Polish", "Polish"),
    )
    # Fields
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=150, blank=False, null=False)
    category = models.ForeignKey(Category, default=Category, on_delete=models.CASCADE)
    price = models.DecimalField(null=False, blank=False, max_digits=7, decimal_places=2, default='9.99')
    language = models.CharField(max_length=50 ,choices=LANGUAGE, default=LANGUAGE)
    short_description = models.TextField(blank=False, null=False, max_length=500, default='')
    description = models.TextField(blank=False, null=False, default='')
    image_preview = OptimizedImageField(upload_to='image_library_preview/%Y/%m/%d/', blank=False, null=False, default='')
    video_preview = models.FileField(upload_to='video_library_preview/%Y/%m/%d/', blank=False, null=False, default='')
    file_download = models.FileField(upload_to='files_library/%Y/%m/%d/', blank=False, null=False, default='')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title