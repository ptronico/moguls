import faker
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.utils import timezone

from apps.events.models import Event
from apps.participants.models import Participant
from apps.scores.models import Score


class Command(BaseCommand):
    """
    This command populates the development environment with seed data.
    You can pass the number of events and participants by arguments.

    It only runs when:
        - `DEBUG=True`
        - There is no events
        - There is no participants
        - Tehre is no scores
    """

    help = "Populates Events, Participants and Scores"

    def add_arguments(self, parser):
        parser.add_argument(
            "--events",
            type=int,
            default=5,
            help="Number of events to create",
        )
        parser.add_argument(
            "--participants",
            type=int,
            default=100,
            help="Number of participants to each event",
        )

    @transaction.atomic
    def handle(self, *args, **options):
        if not settings.DEBUG:
            raise CommandError("This command is not allowed to run when DEBUG is False.")

        events = options.get("events")
        participants = options.get("participants")

        if events_count := Event.objects.all().count():
            raise CommandError(f"{events_count} events already exist in database.")

        if participants_count := Participant.objects.all().count():
            raise CommandError(f"{participants_count} participants already exist in database.")

        if scores_count := Score.objects.all().count():
            raise CommandError(f"{scores_count} scores already exist in database.")

        fake = faker.Faker()
        unique_participants = set()
        event_date = timezone.now().replace(day=1, hour=0, minute=0, microsecond=0)
        for _event_idx in range(events):
            event_date = (event_date - timezone.timedelta(days=1)).replace(day=1)
            event = Event.objects.create(
                name=f"Event {event_date.strftime('%B %Y')}",
                date=event_date,
            )
            for _participant_idx in range(participants):
                # Picking a random first and last name for a Participant. As we do
                # not allow participants with same full name, we will do a limited
                # number of attempts to get a unique name.
                for _full_name_idx in range(100):
                    first_name, last_name = fake.first_name(), fake.last_name()
                    full_name = f"{first_name} {last_name}"
                    if full_name not in unique_participants:
                        unique_participants.add(full_name)
                        break
                participant = Participant.objects.create(first_name=first_name, last_name=last_name)
                # Narrow the range of scores so it helps to more easly identify
                # the propper order on event ranking page.
                air_score = fake.pydecimal(min_value=18.1, max_value=20, right_digits=1)
                turns_score = fake.pydecimal(min_value=58.1, max_value=60, right_digits=1)
                time_score = fake.pydecimal(min_value=18.1, max_value=20, right_digits=1)
                score = Score.objects.create(
                    participant=participant,
                    event=event,
                    air_score=air_score,
                    turns_score=turns_score,
                    time_score=time_score,
                )
                self.stdout.write(
                    self.style.SUCCESS(f"Event: {event} | Participant: {participant} | Score: {score}"),
                )
