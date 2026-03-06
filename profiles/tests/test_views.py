# profiles/tests/test_views.py
"""
View tests for the profiles application.

Light integration tests:
- status codes
- templates used
- a couple of stable HTML contents
"""

import pytest
from django.contrib.auth.models import User
from django.urls import reverse

from profiles.models import Profile


@pytest.mark.django_db
def test_profiles_index_returns_200_and_uses_template(client):
    """GET /profiles/ returns 200 and uses profiles/index.html."""
    url = reverse("profiles:index")
    response = client.get(url)
    assert response.status_code == 200
    assert "profiles/index.html" in [t.name for t in response.templates]


@pytest.mark.django_db
def test_profiles_index_shows_username(client):
    """Profiles index page displays an existing username."""
    user = User.objects.create_user(username="charlie", password="password")
    Profile.objects.create(user=user, favorite_city="Paris")

    url = reverse("profiles:index")
    response = client.get(url)

    assert response.status_code == 200
    assert b"charlie" in response.content


@pytest.mark.django_db
def test_profile_detail_returns_200_and_uses_template(client):
    """Profile detail returns 200 and uses profiles/profile.html."""
    user = User.objects.create_user(username="diana", password="password")
    Profile.objects.create(user=user, favorite_city="Lyon")

    url = reverse("profiles:profile", kwargs={"username": "diana"})
    response = client.get(url)

    assert response.status_code == 200
    assert "profiles/profile.html" in [t.name for t in response.templates]
    assert b"diana" in response.content
