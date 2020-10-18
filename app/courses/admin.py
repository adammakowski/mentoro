from django.contrib import admin
from .models import Course, CourseCategory, CourseLanguage, CourseLesson

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'language', 'price', 'created_date', 'published_date')
    list_filter = ('price', 'language', 'created_date', 'published_date')
    search_fields = ('title',)
    history_list_display = ('title')
    list_per_page = 50

admin.site.register(CourseCategory)
admin.site.register(CourseLanguage)
admin.site.register(CourseLesson)