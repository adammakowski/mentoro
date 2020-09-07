from django.contrib import admin
from .models import Library, Category, Language, Comment
from simple_history.admin import SimpleHistoryAdmin

@admin.register(Library)
class LibraryAdmin(SimpleHistoryAdmin):
    list_display = ('title', 'category', 'author', 'language', 'price', 'created_date', 'published_date')
    list_filter = ('price', 'language', 'created_date', 'published_date')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    history_list_display = ('title')
    list_per_page = 50

admin.site.register(Category, SimpleHistoryAdmin)
admin.site.register(Language, SimpleHistoryAdmin)

@admin.register(Comment)
class CommentAdmin(SimpleHistoryAdmin):
    list_display = ('author', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('author', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)