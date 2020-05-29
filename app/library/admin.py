from django.contrib import admin
from .models import LibraryFile, LibraryCategory, LibraryLanguage
from simple_history.admin import SimpleHistoryAdmin

@admin.register(LibraryFile)
class LibraryFileAdmin(SimpleHistoryAdmin):
    list_display = ('title', 'category', 'author', 'language', 'price', 'created_date', 'published_date')
    list_filter = ('price', 'language', 'created_date', 'published_date')
    search_fields = ('title',)
    history_list_display = ('title')
    list_per_page = 50

admin.site.register(LibraryCategory, SimpleHistoryAdmin)
admin.site.register(LibraryLanguage, SimpleHistoryAdmin)