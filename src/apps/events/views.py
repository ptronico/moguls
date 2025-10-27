from django.shortcuts import render

from .models import Event


def list_events(request):
    events = Event.objects.filter().order_by("-id")
    return render(request, "events.html", context={"events": events})
