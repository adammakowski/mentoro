from django.contrib import admin
from .models import Public
from simple_history.admin import SimpleHistoryAdmin

@admin.register(Public)
class PublicAdmin(SimpleHistoryAdmin):
    actions = ['approve_public_profiles']

    def approve_public_profiles(self, request, queryset):
        queryset.update(active=True)
