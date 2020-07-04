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
    title = models.CharField(max_length=200, blank=False, null=False)
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    language = models.ForeignKey(CourseLanguage, on_delete=models.CASCADE)
    price = models.DecimalField(null=False, blank=False, max_digits=7, decimal_places=2, default='49.99')
    short_description = RichTextField(blank=False, null=False)
    description = RichTextField(blank=False, null=False)
    image_preview = OptimizedImageField(upload_to='courses/image_course_preview/%Y/%m/%d/', blank=False, null=False)
    video_preview = models.FileField(upload_to='courses/image_course_preview/%Y/%m/%d/', blank=False, null=False)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    history = HistoricalRecords()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title