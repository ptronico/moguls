from django.contrib import admin

from .models import Score


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ["id", "participant", "total_score", "air_score", "turns_score", "time_score"]
