from django.db import models

from apps.commons.models import BaseModel


class ScoreManager(models.Manager):
    def get_queryset(self):
        annotations = {
            "total_score_sql": models.ExpressionWrapper(
                models.F("air_score") + models.F("turns_score") + models.F("time_score"),
                output_field=models.FloatField(),
            ),
        }
        return super().get_queryset().annotate(**annotations)


class Score(BaseModel):
    event = models.ForeignKey("events.Event", on_delete=models.CASCADE)
    participant = models.ForeignKey("participants.Participant", on_delete=models.CASCADE)
    air_score = models.FloatField(null=True, default=None, blank=True)
    turns_score = models.FloatField(null=True, default=None, blank=True)
    time_score = models.FloatField(null=True, default=None, blank=True)
    objects = ScoreManager()

    def __str__(self):
        return f"{self.id}"

    @property
    def total_score(self):
        return (self.air_score or 0) + (self.turns_score or 0) + (self.time_score or 0)
