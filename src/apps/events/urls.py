from django.urls import path

from .views import list_events

urlpatterns = [
    path("events/", list_events, name="events"),
]
