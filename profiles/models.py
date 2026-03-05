# profiles/models.py
"""
Models for the profiles application.

This module defines the user profile model linked to Django's
authentication system.
"""

from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """
    Represents a user profile associated with a Django User.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Return the username for display.
        """
        return self.user.username