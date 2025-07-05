from pathlib import Path


class StaticFileSettings:
    BASE_DIR = Path(__file__).resolve().parent.parent

    STATIC_URL = "static/"
    STATIC_ROOT = BASE_DIR / "staticfiles"

    MEDIA_URL = "/media/"
    MEDIA_ROOT = BASE_DIR / "media"
