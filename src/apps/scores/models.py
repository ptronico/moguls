import decimal

from django.db import models
from django.db.models.functions import Cast, Coalesce, Round

from apps.commons.models import BaseModel


class ScoreManager(models.Manager):
    def get_queryset(self):
        """
        Return The default queryset for the `Store` model includes a calculated `_total_score`
        field with the sum of `air_score`, `turns_score` and `time_score`.
        """
        """
        Returns the default queryset for the `Score` model with an extra annotated
        field named `total_score_sql`, which represents the sum of `air_score`,
        `turns_score`, and `time_score`.

        Each component score is:
        - Cast to a DecimalField with a precision of one decimal place
        - Coalesced to zero if it is NULL
        - Rounded to a single decimal place after the summation

        This annotation ensures a consistent and database-level calculation of
        the total score.

        NOTE: SqLite does not have the decimal type. For this it will output
        values like `Decimal('99.9000000000000')`. A later improvement is to
        handle this by transform or quantize it to 1 decimal place.
        """
        annotations = {
            "total_score_sql": Round(
                Cast(
                    Coalesce(models.F("air_score"), 0),
                    output_field=models.DecimalField(max_digits=4, decimal_places=1),
                )
                + Cast(
                    Coalesce(models.F("turns_score"), 0),
                    output_field=models.DecimalField(max_digits=4, decimal_places=1),
                )
                + Cast(
                    Coalesce(models.F("time_score"), 0),
                    output_field=models.DecimalField(max_digits=4, decimal_places=1),
                ),
                1,
            ),
        }
        return super().get_queryset().annotate(**annotations)

    def get_default_ranking(self, event_id: int):
        filters = {
            "event": event_id,
        }
        order_by = [
            "-total_score_sql",
            "-air_score",
            "-turns_score",
            "time_score",
            "participant__last_name",
        ]
        select_related = [
            "participant",
        ]
        return self.get_queryset().filter(**filters).select_related(*select_related).order_by(*order_by)


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
        """
        Total score calculated by summing `air_score`, `turns_score` and `time_score`.

        If the model was instantiated from a queryset and it has the `total_score_sql`
        from the custom manager, use its value.
        """
        total_score_sql = getattr(self, "total_score_sql", None)
        if total_score_sql is not None:
            return total_score_sql.quantize(decimal.Decimal("0.1"))
        return sum(
            [
                self.air_score or decimal.Decimal(),
                self.turns_score or decimal.Decimal(),
                self.time_score or decimal.Decimal(),
            ]
        )
