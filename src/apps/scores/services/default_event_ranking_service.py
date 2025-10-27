import logging

from apps.scores.models import Score

logger = logging.getLogger(__name__)


class DefaultEventRankingService:
    def __init__(self):
        pass

    def execute(self, event_id: int):
        """
        Returns the ranking by default criteria for the given `event_id`.
        """
        filters = {
            "event": event_id,
        }
        order_by = [
            "-total_score_sql",
            "-air_score",
            "-turns_score",
            "time_score",
            "participant__last_name",
        ]
        select_related = [
            "participant",
        ]
        return Score.objects.filter(**filters).select_related(*select_related).order_by(*order_by)
