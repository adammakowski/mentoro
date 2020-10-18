from django.contrib import admin
from .models import Public

@admin.register(Public)
class PublicAdmin(admin.ModelAdmin):
    actions = ['approve_public_profiles']

    def approve_public_profiles(self, request, queryset):
        queryset.update(active=True)
