from core.settings._base import BaseSettings


class Production(
    BaseSettings,
):
    DEBUG = False
