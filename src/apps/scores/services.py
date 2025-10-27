from .models import Score


def get_ranking(event_id: int):
    """
    Returns the ranking by default criteria for the given `event_id.
    """
    filters = {
        "event": event_id,
    }
    order_by = [
        "-total_score",
        "-air_score",
        "-turns_score",
        "time_score",
        "participant__last_name",
    ]
    select_related = [
        "participant",
    ]
    return Score.objects.filter(**filters).select_related(*select_related).order_by(*order_by)
