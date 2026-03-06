# oc_lettings_site/settings.py
"""Django settings for the OCL project."""

import logging
import os
from pathlib import Path

import sentry_sdk
from dotenv import load_dotenv
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.logging import LoggingIntegration

load_dotenv()

# ---------------------------------------------------------
# Sentry configuration
# ---------------------------------------------------------

SENTRY_DSN = os.environ.get("SENTRY_DSN")

sentry_logging = LoggingIntegration(
    level=logging.INFO,
    event_level=logging.ERROR,
)

sentry_sdk.init(
    dsn=SENTRY_DSN,
    integrations=[
        DjangoIntegration(),
        sentry_logging,
    ],
    traces_sample_rate=1.0,
    send_default_pii=True,
)

# ---------------------------------------------------------
# Base configuration
# ---------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "fp$9^593hsriajg$_%=5trot9g!1qa@ew(o-1#@=&4%=hp46(s"

DEBUG = True
ALLOWED_HOSTS = []

# ---------------------------------------------------------
# Application definition
# ---------------------------------------------------------

INSTALLED_APPS = [
    "oc_lettings_site.apps.OCLettingsSiteConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "lettings",
    "profiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "oc_lettings_site.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "oc_lettings_site.wsgi.application"

# ---------------------------------------------------------
# Database
# ---------------------------------------------------------

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "oc-lettings-site.sqlite3"),
    }
}

# ---------------------------------------------------------
# Password validation
# ---------------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ---------------------------------------------------------
# Internationalization
# ---------------------------------------------------------

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True
USE_TZ = True

# ---------------------------------------------------------
# Static files
# ---------------------------------------------------------

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

# ---------------------------------------------------------
# Logging configuration
# ---------------------------------------------------------
# Configure application logging.
# Logs are written to the console for local debugging and
# captured by Sentry through the LoggingIntegration.
#
# Log levels:
# INFO     - normal application activity
# WARNING  - unexpected but non-critical situations
# ERROR    - application errors (sent to Sentry)
# CRITICAL - serious failures
#
# Application loggers are defined per module to control
# verbosity and keep Django internal logs at WARNING level.

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,

    "formatters": {
        "simple": {
            "format": "[{levelname}] {asctime} {name} : {message}",
            "style": "{",
        },
    },

    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
    },

    "loggers": {
        "oc_lettings_site": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
        "lettings": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
        "profiles": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
    },

    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
}
