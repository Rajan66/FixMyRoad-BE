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

    ward = models.ForeignKey(
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

    priority = models.CharField(
        max_length=40,
        choices=ClusterStatus.PRIORITY_CHOICES,
        default="low",
    )

    system_flag = models.CharField(
        max_length=40,
        choices=ClusterStatus.FLAG_CHOICES,
        default="needs_review",
    )

    priority_score = models.FloatField(default=0.0)

    assigned_date = models.DateField(
        null=True,
        blank=True,
    )
