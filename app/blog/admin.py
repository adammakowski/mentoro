from django.contrib import admin
from .models import Post, Category, Language, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'author', 'language', 'created_date', 'published_date')
    list_filter = ('language', 'created_date', 'published_date', 'status')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    history_list_display = ('title')
    list_per_page = 50

admin.site.register(Category)
admin.site.register(Language)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)