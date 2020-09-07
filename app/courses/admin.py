from django.contrib import admin
from .models import Course, CourseCategory, CourseLanguage, CourseLesson
from simple_history.admin import SimpleHistoryAdmin

@admin.register(Course)
class CourseAdmin(SimpleHistoryAdmin):
    list_display = ('title', 'category', 'author', 'language', 'price', 'created_date', 'published_date')
    list_filter = ('price', 'language', 'created_date', 'published_date')
    search_fields = ('title',)
    history_list_display = ('title')
    list_per_page = 50

admin.site.register(CourseCategory, SimpleHistoryAdmin)
admin.site.register(CourseLanguage, SimpleHistoryAdmin)
admin.site.register(CourseLesson, SimpleHistoryAdmin)