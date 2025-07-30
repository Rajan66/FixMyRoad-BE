from _user.models.user import User
from base.models import AbstractBaseModel
from django.db import models


class Ward(AbstractBaseModel):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="ward",
    )

    name = models.CharField(
        max_length=100,
    )

    ward_number = models.CharField(
        max_length=10,
    )

    phone = models.CharField(
        max_length=10,
        null=True,
    )
    # Geolocation (need to think about this)
    area_boundary = models.JSONField(blank=True, null=True)

    image = models.ImageField(
        upload_to="ward/",
        blank=True,
        null=True,
    )

    # dynamically calucate from the geolocation in the future
    location = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.name} - {self.ward_number}"
