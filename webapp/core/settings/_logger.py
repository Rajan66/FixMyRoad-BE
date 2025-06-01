class DevelopmentLogging:
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "verbose": {
                "format": "[{asctime}s] PID: {process:d } [{levelname}s] {message}s",
                "style": "{",
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
            },
        },
        "loggers": {
            "django": {
                "handlers": ["console"],
                "level": "INFO",
                "propagate": True,
                "formatter": "verbose",
            },
            "django.db.backends": {
                "handlers": ["console"],
                "level": "INFO",  # Set to INFO if you don't want raw SQL
            },
        },
    }
