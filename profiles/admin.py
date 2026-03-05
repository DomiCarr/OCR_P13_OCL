# profiles/admin.py
"""
Admin configuration for the profiles application.

Registers the Profile model for management in the Django admin site.
"""

from django.contrib import admin

from profiles.models import Profile


admin.site.register(Profile)
