from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "_user"

    # def ready(self):
    # from services._user import create_user_profile
