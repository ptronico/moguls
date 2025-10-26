from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # uid = models.UUIDField()
    # deleted_at = models.DateTimeField(null=True, blank=True, default=None)
    # is_published = models.BooleanField(default=True)

    class Meta:
        abstract = True
