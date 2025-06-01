from core.settings._base import BaseSettings
from core.settings._logger import DevelopmentLogging
from core.settings._swagger import SwaggerSettings


class Development(
    BaseSettings,
    DevelopmentLogging,
    SwaggerSettings,
):
    DEBUG = True
