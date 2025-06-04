import os
from datetime import timedelta


class TokenSettings:
    SIMPLE_JWT = {
        "ACCESS_TOKEN_LIFETIME": timedelta(
            days=int(
                os.getenv("ACCESS_TOKEN_EXPIRY"),
            )
        ),
        "REFRESH_TOKEN_LIFETIME": timedelta(
            days=int(
                os.getenv("REFRESH_TOKEN_EXPIRY"),
            )
        ),
        "ROTATE_REFRESH_TOKENS": True,
        "BLACKLIST_AFTER_ROTATION": True,
        "AUTH_HEADER_TYPES": ("Bearer",),
        "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    }
