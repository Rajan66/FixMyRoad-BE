from core.settings._defaults import Defaults as D


class AppsSettings:
    INSTALLED_APPS = D.INSTALLED_APPS + [
        "_user"
        # custom apps
    ]
