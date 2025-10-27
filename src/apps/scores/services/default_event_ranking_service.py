import logging

from apps.events.models import Event
from apps.scores.models import Score

logger = logging.getLogger(__name__)


class DefaultEventRankingService:
    """
    Returns a queryset of the ranking for a given event.

    NOTE: there might be a considerable room of future
    improvements, for reducing coupling by passing dependencies
    by arguments (i.e. injecting a repository) and returning
    data transfer objects instead of a model queryset.
    """

    def __init__(self):
        pass

    def execute(self, event_id: int):
        """
        Returns the ranking by default criteria for the given `event_id`.
        """
        if not Event.objects.filter(id=event_id).exists():
            raise ValueError("`event_id` must have a valid Event ID value.")
        return Score.objects.get_default_ranking(event_id=event_id)
