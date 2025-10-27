import decimal

from django.db import models
from django.db.models.functions import Cast, Coalesce, Round

from apps.commons.models import BaseModel


class ScoreManager(models.Manager):
    def get_queryset(self):
        """
        Returns the default queryset for the `Score` model with an annotated field
        named `total_score_sql`, representing the sum of `air_score`, `turns_score`,
        and `time_score`.

        Each component score is:
            - Cast to a DecimalField with one decimal place
            - Coalesced to zero if NULL
            - Rounded to a single decimal place after summation

        This provides a consistent, database-level calculation of the total score.

        NOTE: SQLite does not support a native decimal type, so the annotated result
        may render as values like `Decimal('99.9000000000000')`. A later improvement
        will properly quantize or transform this to one decimal place at the ORM
        level (currently handled by a model property).
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
        """
        Executes the query and applies ordering at the database level
        for better performance. The ranking is determined by multiple
        fields, including a calculated field `total_score_sql` and a
        related field `participant__last_name`.

        Each ranking is scoped by `event_id`, which significantly reduces
        the result set and allows efficient filtering and joins without
        requiring additional indexes beyond `event_id`.

        If requirements change or further optimization is needed, the
        `total_score_sql` and `participant_last_name` fields could be
        materialized in the score table and combined into a composite
        index (in the same order as the ORDER BY clause). This would
        allow the database to serve the query directly from the index
        and return results even faster.

        NOTE: The `id` field is added as the final tie-breaker to ensure
        stable ordering. Without it, pagination could cause some records
        with identical scores to be skipped or not consistently returned.
        """
        filters = {
            "event": event_id,
        }
        order_by = [
            "-total_score_sql",
            "-air_score",
            "-turns_score",
            "time_score",
            "participant__last_name",
            "id",
        ]
        select_related = [
            "participant",
        ]
        return self.get_queryset().filter(**filters).select_related(*select_related).order_by(*order_by)


class Score(BaseModel):
    class Meta:
        """
        Added index to `event` column as each ranking listing result
        is per event. The default ordering is based in the primary key.
        """

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
        Total score computed as the sum of air_score, turns_score, and time_score.

        If the instance was loaded from a queryset annotated with `total_score_sql`,
        that value is used instead.
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
