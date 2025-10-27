from django.urls import path

from .views import AddScoreView, event_ranking_view

urlpatterns = [
    path("events/<int:event_id>/add-score/", AddScoreView.as_view(), name="add_score"),
    path("events/<int:event_id>/ranking/", event_ranking_view, name="ranking"),
]
