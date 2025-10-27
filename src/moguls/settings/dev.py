from .base import *  # noqa: F403


INTERNAL_IPS = [
    "127.0.0.1",
]


INSTALLED_APPS += [  # noqa: F405
    "debug_toolbar",
]


MIDDLEWARE += [  # noqa: F405
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "[{asctime}] [{levelname}] ({name}) {message}",
            "style": "{",
        },
    },
    "handlers": {
        "stdout": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "level": "DEBUG",
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": BASE_DIR / "moguls.log",  # noqa: F405
            "formatter": "default",
            "level": "DEBUG",
        },
    },
    # "root": {
    #     "handlers": ["stdout"],
    #     "level": "ERROR",
    # },
    "loggers": {
        "apps": {
            "handlers": ["file"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}
