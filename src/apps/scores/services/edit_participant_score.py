import logging

from apps.scores.models import Score

logger = logging.getLogger(__name__)


class EditParticipantScoreService:
    def __init__(self):
        pass

    def execute(self, score_id: int, air_score: float, turns_score: float, time_score: float):
        if air_score < 0 or air_score > 20:
            raise ValueError("`air_score` must have a value between 0 and 20.")

        if turns_score < 0 or turns_score > 60:
            raise ValueError("`turns_score` must have a value between 0 and 60.")

        if time_score < 0 or time_score > 20:
            raise ValueError("`time_score` must have a value between 0 and 20.")

        edit_data = {
            "air_score": air_score,
            "turns_score": turns_score,
            "time_score": time_score,
        }
        logger.info(f"Editing #{score_id} score object.", extra=edit_data)
        return Score.objects.filter(id=score_id).update(**edit_data)
