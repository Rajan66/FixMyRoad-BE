from base.enums import ClusterStatus
from base.models import AbstractBaseModel
from django.db import models
from ward.models import Ward


class Cluster(AbstractBaseModel):
    center_longitude = models.FloatField()

    center_latitude = models.FloatField()

    title = models.CharField(
        null=True,
        blank=True,
    )

    ward = models.OneToOneField(
        Ward,
        on_delete=models.SET_NULL,
        related_name="clusters",
        null=True,
        blank=True,
    )

    status = models.CharField(
        max_length=20,
        choices=ClusterStatus.STATUS_CHOICES,
        default="new",
    )

    assigned_date = models.DateField(
        null=True,
        blank=True,
    )
