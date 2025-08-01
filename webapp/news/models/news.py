from _user.models import User
from base.models import AbstractBaseModel
from django.db import models
from ward.models import Ward


class News(AbstractBaseModel):
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
    )

    ward = models.ForeignKey(
        Ward,
        on_delete=models.SET_NULL,
        null=True,
    )

    title = models.CharField(max_length=255)

    content = models.TextField()

    image = models.ImageField(
        upload_to="news/",
        blank=True,
        null=True,
    )
