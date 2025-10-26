from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save

from apps.commons.models import BaseModel


class Score(BaseModel):
    participant = models.ForeignKey("participants.Participant", null=True, on_delete=models.SET_NULL, default=None)
    event = models.ForeignKey("events.Event", null=True, on_delete=models.SET_NULL, default=None)
    # The `turns_score` and `air_score` are calculated by differnt judges and
    # can become available in different times.
    turns_score = models.FloatField(null=True, default=None, blank=True)
    air_score = models.FloatField(null=True, default=None, blank=True)
    # The `time_score` might be calculated automatically by sensors and
    # inputed by an API or external system at a different time.
    time_score = models.FloatField(null=True, default=None, blank=True)
    # The `total_score` is calculated from the sum of `turns_score`, `air_score` and `time_score`.
    # So it only can be calculated when these are available.
    total_score = models.FloatField(null=True, default=None, blank=True)

    def __str__(self):
        return f"{self.id}"


@receiver(pre_save, sender=Score)
def compute_total_score(sender, **kwargs):
    # print(sender)
    # print(kwargs)
    instance = kwargs.get("instance", None)
    if (
        instance
        and instance.turns_score is not None
        and instance.air_score is not None
        and instance.time_score is not None
    ):
        instance.total_score = sum(
            [
                instance.turns_score,
                instance.air_score,
                instance.time_score,
            ]
        )
