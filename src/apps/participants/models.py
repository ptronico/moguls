from django.db import models

from apps.commons.models import BaseModel


class Participant(BaseModel):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
