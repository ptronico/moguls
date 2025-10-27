from apps.scores.models import Score


class AddParticipantScoreService:
    def __init__(self):
        pass

    def execute(self, event_id: int, participant_id: int, air_score: float, turns_score: float, time_score: float):
        total_score = sum(
            [
                air_score,
                turns_score,
                time_score,
            ]
        )
        Score.objects.create(
            event_id=event_id,
            participant_id=participant_id,
            air_score=air_score,
            turns_score=turns_score,
            time_score=time_score,
            total_score=total_score,
        )
