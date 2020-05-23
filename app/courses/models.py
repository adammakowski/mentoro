from django.db import models
from django.utils import timezone
from optimized_image.fields import OptimizedImageField

class Course(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False, null=False)
    price = models.DecimalField(null=False, blank=False, max_digits=7, decimal_places=2, default='99.99')
    short_description = models.TextField(blank=False, null=False, max_length=400, default='')
    description = models.TextField(blank=False, null=False, default='')
    image_preview = OptimizedImageField(upload_to='image_course_preview/%Y/%m/%d/', blank=False, null=False, default='')
    video_preview = models.FileField(upload_to='video_course_preview/%Y/%m/%d/', blank=False, null=False, default='')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title