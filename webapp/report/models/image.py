from base.models import AbstractBaseModel
from django.db import models

from report.models import PotholeReport


class PotholeImage(AbstractBaseModel):
    report = models.ForeignKey(
        PotholeReport,
        on_delete=models.CASCADE,
        related_name="report",
    )

    image = models.ImageField(
        upload_to="pothole_images/",
    )

    def __str__(self):
        return f"Image {self.id} for Report {self.report.title}"
