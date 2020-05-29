from django.db import models
from django.utils import timezone
from optimized_image.fields import OptimizedImageField
from simple_history.models import HistoricalRecords

class LibraryCategory(models.Model):
    title = models.CharField(max_length=150, default='', blank=False, null=False)
    history = HistoricalRecords()

    def __str__(self):
        return self.title

class LibraryLanguage(models.Model):
    title = models.CharField(max_length=150, default='', blank=False, null=False)
    history = HistoricalRecords()

    def __str__(self):
        return self.title

class LibraryFile(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=150, blank=False, null=False, default='')
    category = models.ForeignKey(LibraryCategory, default='', on_delete=models.CASCADE)
    language = models.ForeignKey(LibraryLanguage, default='', on_delete=models.CASCADE)
    price = models.DecimalField(null=False, blank=False, max_digits=7, decimal_places=2, default='9.99')
    short_description = models.TextField(blank=False, null=False, max_length=500, default='')
    description = models.TextField(blank=False, null=False, default='')
    image_preview = OptimizedImageField(upload_to='library/image_library_preview/%Y/%m/%d/', blank=False, null=False, default='')
    video_preview = models.FileField(upload_to='library/video_library_preview/%Y/%m/%d/', blank=True, null=True, default='')
    file_download = models.FileField(upload_to='library/files_library/%Y/%m/%d/', blank=False, null=False, default='')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)
    history = HistoricalRecords()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title