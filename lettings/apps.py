# lettings/apps.py
"""Application configuration for the lettings app."""

from django.apps import AppConfig


class LettingsConfig(AppConfig):
    """Django AppConfig for the lettings application."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "lettings"