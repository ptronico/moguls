from django.db import models

from apps.commons.models import BaseModel


class Event(BaseModel):
    name = models.CharField(max_length=100)
    date = models.DateField(null=True, default=None)

    class Meta:
        ordering = ["-date", "-id"]

    def __str__(self):
        return f"{self.name}"
