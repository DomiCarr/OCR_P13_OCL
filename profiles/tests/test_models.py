# profiles/tests/test_models.py
"""
Model tests for the profiles application.

These tests focus on custom behavior (e.g., __str__) without over-testing
Django's ORM.
"""

import pytest
from django.contrib.auth.models import User

from profiles.models import Profile


@pytest.mark.django_db
def test_profile_str():
    """Profile.__str__ returns the related username."""
    user = User.objects.create_user(username="alice", password="password")
    profile = Profile.objects.create(user=user, favorite_city="Paris")
    assert str(profile) == "alice"


@pytest.mark.django_db
def test_profile_favorite_city_can_be_blank():
    """favorite_city can be blank (empty string) as per model definition."""
    user = User.objects.create_user(username="bob", password="password")
    profile = Profile.objects.create(user=user, favorite_city="")
    assert profile.favorite_city == ""
