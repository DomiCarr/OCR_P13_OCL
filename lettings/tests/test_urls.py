# lettings/tests/test_urls.py
"""
Tests for lettings URL routing.

These tests validate URL names and namespaces for the lettings app.
"""

from django.urls import reverse


def test_reverse_lettings_index():
    """reverse() should resolve the lettings index URL."""
    assert reverse("lettings:index") == "/lettings/"


def test_reverse_letting_detail():
    """reverse() should resolve the letting detail URL with an id."""
    assert reverse("lettings:letting", kwargs={"letting_id": 1}) == "/lettings/1/"