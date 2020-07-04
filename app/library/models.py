from django.db import models
from django.utils import timezone
from optimized_image.fields import OptimizedImageField
from simple_history.models import HistoricalRecords
from ckeditor.fields import RichTextField

class LibraryCategory(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    history = HistoricalRecords()

    def __str__(self):
        return self.title

class LibraryLanguage(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    history = HistoricalRecords()

    def __str__(self):
        return self.title

class LibraryFile(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=150, blank=False, null=False)
    category = models.ForeignKey(LibraryCategory, on_delete=models.CASCADE)
    language = models.ForeignKey(LibraryLanguage, on_delete=models.CASCADE)
    price = models.DecimalField(null=False, blank=False, max_digits=7, decimal_places=2)
    short_description = RichTextField(blank=False, null=False, max_length=500)
    description = RichTextField(blank=False, null=False)
    contests = RichTextField(blank=False, null=False)
    requirements = RichTextField(blank=False, null=False)
    image_preview = OptimizedImageField(upload_to='library/image_library_preview/%Y/%m/%d/', blank=False, null=False)
    video_preview = models.FileField(upload_to='library/video_library_preview/%Y/%m/%d/', blank=True, null=True)
    file_download = models.FileField(upload_to='library/files_library/%Y/%m/%d/', blank=False, null=False)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)
    history = HistoricalRecords()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title