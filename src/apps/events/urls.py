from django.urls import path
from django.views.generic import RedirectView

from .views import list_events

urlpatterns = [
    path("", RedirectView.as_view(url="events/")),
    path("events/", list_events, name="events"),
]
