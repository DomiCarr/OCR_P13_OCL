# oc_lettings_site/tests/test_urls.py
"""
Tests for project-level URL routing.

These tests ensure that named URL patterns can be reversed correctly.
"""

from django.urls import reverse


def test_reverse_index():
    """reverse() should resolve the homepage URL."""
    assert reverse("index") == "/"