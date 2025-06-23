from configurations import Configuration

from core.settings._apps import AppsSettings
from core.settings._cors import CorsSettings
from core.settings._database import DatabaseSettings
from core.settings._i18n import I18NSettings
from core.settings._middlewares import MiddlewareSettings
from core.settings._rest_framework import RestFrameworkSettings
from core.settings._security import SecuritySettings
from core.settings._static import StaticFileSettings
from core.settings._swagger import SwaggerSettings
from core.settings._templates import TemplatesSettings
from core.settings._token import TokenSettings
from core.settings._validators import ValidatorsSettings


class BaseSettings(
    AppsSettings,
    CorsSettings,
    MiddlewareSettings,
    DatabaseSettings,
    I18NSettings,
    TemplatesSettings,
    RestFrameworkSettings,
    SecuritySettings,
    ValidatorsSettings,
    StaticFileSettings,
    SwaggerSettings,
    TokenSettings,
    Configuration,
):
    @classmethod
    def post_setup(cls):
        super(BaseSettings, cls).post_setup()
