from _user.models import UserProfile
from base.enums import ReportStatus
from base.models import AbstractBaseModel
from cluster.models import Cluster
from django.db import models


class PotholeReport(AbstractBaseModel):
    profile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name="reports",
        db_index=True,
    )

    # report doesn't need to belong to a cluster right away
    cluster = models.ForeignKey(
        Cluster,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="reports",
    )

    title = models.CharField(
        max_length=255,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    latitude = models.FloatField()

    longitude = models.FloatField()

    status = models.CharField(
        max_length=20,
        choices=ReportStatus.STATUS_CHOICES,
        default="open",
    )

    def __str__(self):
        return f"Report {self.title} by {self.profile.first_name}"
