import faker
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from apps.events.models import Event
from apps.participants.models import Participant
from apps.scores.models import Score


class Command(BaseCommand):
    help = "Populates Events, Participants and Scores"

    def add_arguments(self, parser):
        parser.add_argument(
            "--events",
            type=int,
            default=10,
            help="Number of events to create",
        )
        parser.add_argument(
            "--participants",
            type=int,
            default=100,
            help="Number of participants to each event",
        )

    def handle(self, *args, **options):
        events = options.get("events")
        participants = options.get("participants")

        if events_count := Event.objects.all().count():
            raise CommandError(f"{events_count} events already exist in database.")

        if participants_count := Participant.objects.all().count():
            raise CommandError(f"{participants_count} participants already exist in database.")

        if scores_count := Score.objects.all().count():
            raise CommandError(f"{scores_count} scores already exist in database.")

        fake = faker.Faker()
        event_date = timezone.now().replace(day=1, hour=0, minute=0, microsecond=0)
        for i in range(events):
            event_date = (event_date - timezone.timedelta(days=1)).replace(day=1)
            event = Event.objects.create(
                name=f"Event {event_date.strftime('%B %Y')}",
                date=event_date,
            )
            for j in range(participants):
                participant = Participant.objects.create(
                    first_name=fake.first_name_male(),
                    last_name=fake.last_name_male(),
                )
                turns_score = fake.pyfloat(min_value=0, max_value=60, right_digits=2)
                air_score = fake.pyfloat(min_value=0, max_value=20, right_digits=2)
                time_score = fake.pyfloat(min_value=0, max_value=20, right_digits=2)
                score = Score.objects.create(
                    participant=participant,
                    event=event,
                    turns_score=turns_score,
                    air_score=air_score,
                    time_score=time_score,
                    total_score=turns_score + air_score + time_score,
                )
                self.stdout.write(
                    self.style.SUCCESS(f"Event: {event} | Participant: {participant} | Score: {score}"),
                )

        # for poll_id in options["poll_ids"]:
        #     try:
        #         poll = Poll.objects.get(pk=poll_id)
        #     except Poll.DoesNotExist:
        #         raise CommandError('Poll "%s" does not exist' % poll_id)

        #     poll.opened = False
        #     poll.save()

        #     self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))
