from _user.models import User
from base.models import AbstractBaseModel
from django.db import models


class Ward(AbstractBaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="ward",
    )

    name = models.CharField(
        max_length=20,
    )

    ward_number = models.CharField(
        max_length=10,
    )

    # Geolocation (need to think about this)
    area_boundary = models.JSONField()

    image = models.ImageField(
        upload_to="ward/",
    )

    # dynamically calucate from the geolocation in the future
    town = models.CharField(
        max_length=100,
    )
