from django.contrib import admin
from .models import BlogPost, BlogCategory, BlogLanguage
from simple_history.admin import SimpleHistoryAdmin

@admin.register(BlogPost)
class BlogPostAdmin(SimpleHistoryAdmin):
    list_display = ('title', 'category', 'author', 'language', 'created_date', 'published_date')
    list_filter = ('language', 'created_date', 'published_date')
    search_fields = ('title',)
    history_list_display = ('title')
    list_per_page = 50

admin.site.register(BlogCategory, SimpleHistoryAdmin)
admin.site.register(BlogLanguage, SimpleHistoryAdmin)