# oc_lettings_site/tests/test_homepage.py

"""
Tests for the project homepage.
"""

from django.test import Client


def test_homepage_returns_200():
    """
    Homepage should return HTTP 200.
    """
    client = Client()
    response = client.get("/")
    assert response.status_code == 200