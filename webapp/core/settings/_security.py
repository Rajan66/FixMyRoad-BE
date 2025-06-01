import os

from dotenv import load_dotenv


class SecuritySettings:
    load_dotenv()

    SECRET_KEY = os.getenv("SECRET_KEY")

    ROOT_URLCONF = "core.urls"

    WSGI_APPLICATION = "core.wsgi.application"

    DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

    AUTH_USER_MODEL = "_user.User"
