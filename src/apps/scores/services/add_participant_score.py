import logging

from apps.events.models import Event
from apps.participants.models import Participant
from apps.scores.models import Score

logger = logging.getLogger(__name__)


class AddParticipantScoreService:
    """
    Creates a new score entry for a given participant in a
    given event. The score must follow the business rule for
    the Freestyle Moguls Competition Scoring System.
    """

    def __init__(self):
        pass

    def execute(self, event_id: int, participant_id: int, air_score: float, turns_score: float, time_score: float):
        if air_score < 0 or air_score > 20:
            raise ValueError("`air_score` must have a value between 0 and 20.")

        if turns_score < 0 or turns_score > 60:
            raise ValueError("`turns_score` must have a value between 0 and 60.")

        if time_score < 0 or time_score > 20:
            raise ValueError("`time_score` must have a value between 0 and 20.")

        if not Event.objects.filter(id=event_id).exists():
            raise ValueError("`event_id` must have a valid Event ID value.")

        if not Participant.objects.filter(id=participant_id).exists():
            raise ValueError("`participant_id` must have a valid Participant ID value.")

        new_score_data = {
            "event_id": event_id,
            "participant_id": participant_id,
            "air_score": air_score,
            "turns_score": turns_score,
            "time_score": time_score,
        }
        logger.info("Creating a new score object.", extra=new_score_data)
        return Score.objects.create(**new_score_data)
