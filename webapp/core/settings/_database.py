import os

from dotenv import load_dotenv

load_dotenv()


class DatabaseSettings:
    # Get database settings with validation
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "5432")

    # Validate required variables
    if not DB_NAME:
        raise ValueError("DB_NAME environment variable is required")
    if not DB_USER:
        raise ValueError("DB_USER environment variable is required")

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": DB_NAME,
            "USER": DB_USER,
            "PASSWORD": DB_PASSWORD,
            "HOST": DB_HOST,
            "PORT": DB_PORT,
        }
    }
