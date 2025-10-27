from django.db import models

from apps.commons.models import BaseModel


class Participant(BaseModel):
    class Meta:
        """
        Since only `first_name` and `last_name` are used to identify a participant,
        a composite unique constraint is applied to these two fields (in this
        order). The default ordering also uses them, so a composite index was added
        to improve query performance.
        """

        ordering = ["first_name", "last_name"]
        indexes = [
            models.Index(fields=["first_name", "last_name"], name="full_name_index"),
        ]
        constraints = [
            models.UniqueConstraint(fields=["first_name", "last_name"], name="unique_full_name"),
        ]

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
