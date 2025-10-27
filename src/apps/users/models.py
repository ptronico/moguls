from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Defines a custom user model to allow easier extension
    and customization in the future.
    """

    pass
