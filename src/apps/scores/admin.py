from django.contrib import admin

from .models import Score


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ["id", "participant", "total_score", "air_score", "turns_score", "time_score"]
    list_display_links = ["id"]
    search_fields = ["event__name", "participant__first_name", "participant__last_name"]
    list_filter = ["event", "created_at", "updated_at"]
