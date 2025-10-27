from django.test import TestCase
from django.utils import timezone

from apps.events.models import Event
from apps.participants.models import Participant
from apps.scores.models import Score
from apps.scores.services import AddParticipantScoreService


class RankingByTotalScoreTestCase(TestCase):
    def setUp(self):
        self.event = Event.objects.create(name="Event", date=timezone.now())
        self.aaron_jones = Participant.objects.create(first_name="Aaron", last_name="Jones")

    def test_add_participant_score(self):
        add_participant_score_service = AddParticipantScoreService()
        add_participant_score_service.execute(
            event_id=self.event.id,
            participant_id=self.aaron_jones.id,
            air_score=1,
            turns_score=2,
            time_score=3,
        )
        score = Score.objects.filter(event_id=self.event.id, participant_id=self.aaron_jones.id).get()
        self.assertEqual(score.air_score, 1.0)
        self.assertEqual(score.turns_score, 2.0)
        self.assertEqual(score.time_score, 3.0)
        self.assertEqual(score.total_score, 6.0)

    def test_add_participant_with_wrong_score(self):
        add_participant_score_service = AddParticipantScoreService()
        with self.assertRaises(ValueError):
            add_participant_score_service.execute(
                event_id=self.event.id,
                participant_id=self.aaron_jones.id,
                air_score=100,
                turns_score=200,
                time_score=300,
            )

    def test_add_participant_with_wrong_event_id(self):
        add_participant_score_service = AddParticipantScoreService()
        with self.assertRaises(ValueError):
            add_participant_score_service.execute(
                event_id=None,
                participant_id=self.aaron_jones.id,
                air_score=100,
                turns_score=200,
                time_score=300,
            )

    def test_add_participant_with_wrong_participant_id(self):
        add_participant_score_service = AddParticipantScoreService()
        with self.assertRaises(ValueError):
            add_participant_score_service.execute(
                event_id=self.event.id,
                participant_id=self.aaron_jones.id + 1,
                air_score=1,
                turns_score=1,
                time_score=1,
            )
