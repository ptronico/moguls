from django.contrib import admin

from .models import Participant


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "created_at", "updated_at"]
    list_display_links = ["id"]
    search_fields = ["first_name", "last_name"]
    list_filter = ["created_at", "updated_at"]
