from base.models import AbstractBaseModel
from django.db import models

from .user import User


class UserProfile(AbstractBaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
    )

    first_name = models.CharField(
        max_length=255,
    )

    last_name = models.CharField(
        max_length=255,
    )

    bio = models.TextField(
        blank=True,
        null=True,
    )

    address = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    phone = models.CharField(
        max_length=10,
        blank=True,
        null=True,
    )

    image = models.ImageField(
        upload_to="profile/",
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.user.email}"
