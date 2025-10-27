from django.db import models


class BaseModel(models.Model):
    """
    Base model for all concrete models in the application. Provides
    `created_at` and `updated_at` timestamp fields, and may include
    soft deletes or other common features in the future.
    """

    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
