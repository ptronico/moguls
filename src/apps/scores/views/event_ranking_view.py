from django.shortcuts import render

from apps.events.models import Event
from apps.scores.services import DefaultEventRankingService


def event_ranking_view(request, event_id: int):
    """
    Lists all participants for that event, sorted by total_score (highest first).
        - If two or more participants have the same total score, apply tie-breaking in this order:

    1. Higher air_score wins.
    2. If still tied, higher turns_score wins.
    3. If still tied, shorter time_score wins (faster time).
    4. If still tied after that, sort alphabetically by last_name.

    + adicionar um critério final, pois o last_name pode ser igual.
    """
    event = Event.objects.get(id=event_id)
    default_event_ranking_service = DefaultEventRankingService()
    ranking = default_event_ranking_service.execute(event.id)
    context = {
        "event": event,
        "ranking": ranking,
    }
    return render(request, "ranking.html", context=context)
