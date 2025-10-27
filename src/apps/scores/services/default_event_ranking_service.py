import logging

from django.db.models import ExpressionWrapper, F, FloatField

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
            "-total",
            "-air_score",
            "-turns_score",
            "time_score",
            "participant__last_name",
        ]
        select_related = [
            "participant",
        ]
        annotated = {
            "total": ExpressionWrapper(
                F("air_score") + F("turns_score") + F("time_score"),
                output_field=FloatField(),
            ),
        }
        return Score.objects.filter(**filters).select_related(*select_related).annotate(**annotated).order_by(*order_by)
