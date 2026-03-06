# profiles/apps.py
"""Application configuration for the profiles app."""

from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """Django AppConfig for the profiles application."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "profiles"
