from django.test import TestCase
from django.utils import timezone

from apps.events.models import Event
from apps.participants.models import Participant
from apps.scores.models import Score
from apps.scores.services import DefaultEventRankingService


class RankingByTotalScoreTestCase(TestCase):
    def setUp(self):
        self.event = Event.objects.create(name="Event", date=timezone.now())
        self.first_place = Participant.objects.create(first_name="Aaron", last_name="Jones")
        self.second_place = Participant.objects.create(first_name="Albert", last_name="Jones")
        self.third_place = Participant.objects.create(first_name="Adam", last_name="Jones")
        self.fourth_place = Participant.objects.create(first_name="Alex", last_name="Jones")
        self.fifth_place = Participant.objects.create(first_name="Allison", last_name="Jones")
        scores = [
            (self.first_place, 0, 0, 0, 100),
            (self.third_place, 0, 0, 0, 99),
            (self.fourth_place, 0, 0, 0, 98),
            (self.second_place, 0, 0, 0, 97),
            (self.fifth_place, 0, 0, 0, 96),
        ]
        self.participant_ranking = []
        for participant, air_score, turns_core, time_score, total_score in scores:
            self.participant_ranking.append(participant)
            Score.objects.create(
                event=self.event,
                participant=participant,
                air_score=air_score,
                turns_score=turns_core,
                time_score=time_score,
                total_score=total_score,
            )

    def test_ranking_by_total_score(self):
        default_event_ranking_service = DefaultEventRankingService()
        ranking = default_event_ranking_service.execute(event_id=self.event.id)
        for score, participant in zip(ranking, self.participant_ranking):
            self.assertEqual(score.participant.id, participant.id)


class RankingByAirScoreTestCase(TestCase):
    def setUp(self):
        self.event = Event.objects.create(name="Event", date=timezone.now())
        self.first_place = Participant.objects.create(first_name="Aaron", last_name="Jones")
        self.second_place = Participant.objects.create(first_name="Albert", last_name="Jones")
        self.third_place = Participant.objects.create(first_name="Adam", last_name="Jones")
        self.fourth_place = Participant.objects.create(first_name="Alex", last_name="Jones")
        self.fifth_place = Participant.objects.create(first_name="Allison", last_name="Jones")
        scores = [
            (self.first_place, 20, 0, 0, 0),
            (self.second_place, 19, 0, 0, 0),
            (self.third_place, 18, 0, 0, 0),
            (self.fourth_place, 17, 0, 0, 0),
            (self.fifth_place, 16, 0, 0, 0),
        ]
        self.participant_ranking = []
        for participant, air_score, turns_core, time_score, total_score in scores:
            self.participant_ranking.append(participant)
            Score.objects.create(
                event=self.event,
                participant=participant,
                air_score=air_score,
                turns_score=turns_core,
                time_score=time_score,
                total_score=total_score,
            )

    def test_ranking_by_air_score(self):
        default_event_ranking_service = DefaultEventRankingService()
        ranking = default_event_ranking_service.execute(event_id=self.event.id)
        for score, participant in zip(ranking, self.participant_ranking):
            self.assertEqual(score.participant.id, participant.id)


class RankingByTurnsScoreTestCase(TestCase):
    def setUp(self):
        self.event = Event.objects.create(name="Event", date=timezone.now())
        self.first_place = Participant.objects.create(first_name="Aaron", last_name="Jones")
        self.second_place = Participant.objects.create(first_name="Albert", last_name="Jones")
        self.third_place = Participant.objects.create(first_name="Adam", last_name="Jones")
        self.fourth_place = Participant.objects.create(first_name="Alex", last_name="Jones")
        self.fifth_place = Participant.objects.create(first_name="Allison", last_name="Jones")
        scores = [
            (self.first_place, 0, 60, 0, 0),
            (self.second_place, 0, 59, 0, 0),
            (self.third_place, 0, 58, 0, 0),
            (self.fourth_place, 0, 57, 0, 0),
            (self.fifth_place, 0, 56, 0, 0),
        ]
        self.participant_ranking = []
        for participant, air_score, turns_core, time_score, total_score in scores:
            self.participant_ranking.append(participant)
            Score.objects.create(
                event=self.event,
                participant=participant,
                air_score=air_score,
                turns_score=turns_core,
                time_score=time_score,
                total_score=total_score,
            )

    def test_ranking_by_turns_score(self):
        default_event_ranking_service = DefaultEventRankingService()
        ranking = default_event_ranking_service.execute(event_id=self.event.id)
        for score, participant in zip(ranking, self.participant_ranking):
            self.assertEqual(score.participant.id, participant.id)


class RankingByTimeScoreTestCase(TestCase):
    def setUp(self):
        self.event = Event.objects.create(name="Event", date=timezone.now())
        self.first_place = Participant.objects.create(first_name="Aaron", last_name="Jones")
        self.second_place = Participant.objects.create(first_name="Albert", last_name="Jones")
        self.third_place = Participant.objects.create(first_name="Adam", last_name="Jones")
        self.fourth_place = Participant.objects.create(first_name="Alex", last_name="Jones")
        self.fifth_place = Participant.objects.create(first_name="Allison", last_name="Jones")
        scores = [
            (self.first_place, 0, 0, 15, 0),
            (self.second_place, 0, 0, 16, 0),
            (self.third_place, 0, 0, 17, 0),
            (self.fourth_place, 0, 0, 18, 0),
            (self.fifth_place, 0, 0, 19, 0),
        ]
        self.participant_ranking = []
        for participant, air_score, turns_core, time_score, total_score in scores:
            self.participant_ranking.append(participant)
            Score.objects.create(
                event=self.event,
                participant=participant,
                air_score=air_score,
                turns_score=turns_core,
                time_score=time_score,
                total_score=total_score,
            )

    def test_ranking_by_time_score(self):
        default_event_ranking_service = DefaultEventRankingService()
        ranking = default_event_ranking_service.execute(event_id=self.event.id)
        for score, participant in zip(ranking, self.participant_ranking):
            self.assertEqual(score.participant.id, participant.id)


class RankingByLastNameTestCase(TestCase):
    def setUp(self):
        self.event = Event.objects.create(name="Event", date=timezone.now())
        self.first_place = Participant.objects.create(first_name="Aaron", last_name="A")
        self.second_place = Participant.objects.create(first_name="Albert", last_name="B")
        self.third_place = Participant.objects.create(first_name="Adam", last_name="C")
        self.fourth_place = Participant.objects.create(first_name="Alex", last_name="D")
        self.fifth_place = Participant.objects.create(first_name="Allison", last_name="E")
        scores = [
            (self.first_place, 0, 0, 0, 0),
            (self.second_place, 0, 0, 0, 0),
            (self.third_place, 0, 0, 0, 0),
            (self.fourth_place, 0, 0, 0, 0),
            (self.fifth_place, 0, 0, 0, 0),
        ]
        self.participant_ranking = []
        for participant, air_score, turns_core, time_score, total_score in scores:
            self.participant_ranking.append(participant)
            Score.objects.create(
                event=self.event,
                participant=participant,
                air_score=air_score,
                turns_score=turns_core,
                time_score=time_score,
                total_score=total_score,
            )

    def test_ranking_by_last_name(self):
        default_event_ranking_service = DefaultEventRankingService()
        ranking = default_event_ranking_service.execute(event_id=self.event.id)
        for score, participant in zip(ranking, self.participant_ranking):
            self.assertEqual(score.participant.id, participant.id)
