import decimal

from django.db import models
from django.db.models.functions import Cast, Coalesce, Round

from apps.commons.models import BaseModel


class ScoreManager(models.Manager):
    def get_queryset(self):
        annotations = {
            "total_score_sql": models.ExpressionWrapper(
                Round(
                    Coalesce(Cast(models.F("air_score"), models.DecimalField(max_digits=4, decimal_places=1)), 0)
                    + Coalesce(Cast(models.F("turns_score"), models.DecimalField(max_digits=4, decimal_places=1)), 0)
                    + Coalesce(Cast(models.F("time_score"), models.DecimalField(max_digits=4, decimal_places=1)), 0),
                    1,
                ),
                # models.F("air_score") + models.F("turns_score") + models.F("time_score"),
                output_field=models.DecimalField(max_digits=4, decimal_places=1),
            ),
        }
        return super().get_queryset().annotate(**annotations)


class Score(BaseModel):
    class Meta:
        ordering = ["-id"]
        indexes = [
            models.Index(fields=["event"], name="event_index"),
        ]

    event = models.ForeignKey("events.Event", on_delete=models.CASCADE)
    participant = models.ForeignKey("participants.Participant", on_delete=models.CASCADE)
    air_score = models.DecimalField(max_digits=4, decimal_places=1, null=True, default=None, blank=True)
    turns_score = models.DecimalField(max_digits=4, decimal_places=1, null=True, default=None, blank=True)
    time_score = models.DecimalField(max_digits=4, decimal_places=1, null=True, default=None, blank=True)
    objects = ScoreManager()

    def __str__(self):
        return f"{self.event.name} - {self.participant.full_name} - {self.total_score}"

    @property
    def total_score(self):
        return sum(
            [
                self.air_score or decimal.Decimal(),
                self.turns_score or decimal.Decimal(),
                self.time_score or decimal.Decimal(),
            ]
        )
