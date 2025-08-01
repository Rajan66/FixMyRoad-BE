from _user.models import User
from base.models import AbstractBaseModel
from django.db import models
from report.models import PotholeReport


class Comment(AbstractBaseModel):
    report = models.ForeignKey(
        PotholeReport, on_delete=models.CASCADE, related_name="comments"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return f"Comment by {self.user} on Report #{self.report_id}"
