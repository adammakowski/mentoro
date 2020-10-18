from django.contrib import admin
from .models import Mentor, Category, Language

@admin.register(Mentor)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'active', 'category', 'author', 'language', 'created_date', 'published_date')
    list_filter = ('active', 'language', 'created_date', 'published_date', 'status')
    search_fields = ('title', 'author')
    history_list_display = ('title')
    list_per_page = 50
    actions = ['approve_mentors']

    def approve_mentors(self, request, queryset):
        queryset.update(active=True)

admin.site.register(Category)
admin.site.register(Language)