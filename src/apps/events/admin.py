from django.contrib import admin

from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "date", "created_at", "updated_at"]
    list_display_links = ["id"]
    search_fields = ["name"]
    list_filter = ["created_at", "updated_at"]
