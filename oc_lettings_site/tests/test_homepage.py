# oc_lettings_site/tests/test_homepage.py
"""
Tests for the homepage view.
"""

import pytest
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
def test_homepage_returns_200():
    """Homepage should return HTTP 200."""
    client = Client()
    response = client.get(reverse("index"))

    assert response.status_code == 200


@pytest.mark.django_db
def test_homepage_template_used():
    """Homepage should use the index template."""
    client = Client()
    response = client.get(reverse("index"))

    assert "index.html" in [t.name for t in response.templates]


@pytest.mark.django_db
def test_homepage_contains_links():
    """Homepage should contain navigation links to lettings and profiles."""
    client = Client()
    response = client.get(reverse("index"))

    content = response.content.decode()

    assert "Lettings" in content
    assert "Profiles" in content
