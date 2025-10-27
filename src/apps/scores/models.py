from django.db import models

from apps.commons.models import BaseModel


# class ScoreManager(models.Manager):
#     def create(self, object):


#     def with_counts(self):
#         return self.annotate(num_responses=Coalesce(models.Count("response"), 0))


class Score(BaseModel):
    event = models.ForeignKey("events.Event", on_delete=models.CASCADE)
    participant = models.ForeignKey("participants.Participant", on_delete=models.CASCADE)
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
