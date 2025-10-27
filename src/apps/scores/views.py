from django.shortcuts import render

from .services import get_ranking


def ranking(request, event_id: int):
    """
    Lists all participants for that event, sorted by total_score (highest first).
        - If two or more participants have the same total score, apply tie-breaking in this order:

    1. Higher air_score wins.
    2. If still tied, higher turns_score wins.
    3. If still tied, shorter time_score wins (faster time).
    4. If still tied after that, sort alphabetically by last_name.

    + adicionar um critério final, pois o last_name pode ser igual.
    """
    ranking = get_ranking(event_id=event_id)
    return render(request, "ranking.html", context={"ranking": ranking})
