from django.urls import path

from .views import AddScoreView, EditScoreView, event_ranking_view

urlpatterns = [
    path("events/<int:event_id>/add/", AddScoreView.as_view(), name="add_score"),
    path("events/<int:event_id>/edit/<int:score_id>/", EditScoreView.as_view(), name="edit_score"),
    path("events/<int:event_id>/ranking/", event_ranking_view, name="ranking"),
]
