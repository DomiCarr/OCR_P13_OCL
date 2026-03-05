# profiles/tests/test_urls.py
"""
Tests for profiles URL routing.

These tests validate URL names and namespaces for the profiles app.
"""

from django.urls import reverse


def test_reverse_profiles_index():
    """reverse() should resolve the profiles index URL."""
    assert reverse("profiles:index") == "/profiles/"


def test_reverse_profile_detail():
    """reverse() should resolve the profile detail URL with a username."""
    assert reverse("profiles:profile", kwargs={"username": "john"}) == "/profiles/john/"