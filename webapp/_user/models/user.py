from base.enums import UserRole
from base.models._base import AbstractBaseModel
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from managers._user import CustomUserManager


class User(AbstractBaseUser, AbstractBaseModel, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)  # _ for translation

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    role = models.CharField(
        max_length=20,
        choices=UserRole.USER_ROLES,
        default="user",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
