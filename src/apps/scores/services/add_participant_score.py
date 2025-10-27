import logging

from apps.scores.models import Score

logger = logging.getLogger(__name__)


class AddParticipantScoreService:
    def __init__(self):
        pass

    def execute(self, event_id: int, participant_id: int, air_score: float, turns_score: float, time_score: float):
        new_score_data = {
            "event_id": event_id,
            "participant_id": participant_id,
            "air_score": air_score,
            "turns_score": turns_score,
            "time_score": time_score,
        }
        logger.info("Creating a new score object.", extra=new_score_data)
        return Score.objects.create(**new_score_data)
