# lettings/tests/test_views.py
"""
View tests for the lettings application.

Light integration tests:
- status codes
- templates used
- a couple of stable HTML contents
"""

import pytest
from django.urls import reverse

from lettings.models import Address, Letting


@pytest.mark.django_db
def test_lettings_index_returns_200_and_uses_template(client):
    """GET /lettings/ returns 200 and uses lettings/index.html."""
    url = reverse("lettings:index")
    response = client.get(url)
    assert response.status_code == 200
    assert "lettings/index.html" in [t.name for t in response.templates]


@pytest.mark.django_db
def test_lettings_index_shows_letting_title(client):
    """Lettings index page displays the created letting title."""
    address = Address.objects.create(
        number=10,
        street="Avenue des Tests",
        city="Paris",
        state="FR",
        zip_code=75000,
        country_iso_code="FRA",
    )
    letting = Letting.objects.create(title="Sunny Studio", address=address)

    url = reverse("lettings:index")
    response = client.get(url)

    assert response.status_code == 200
    assert letting.title.encode() in response.content


@pytest.mark.django_db
def test_letting_detail_returns_200_and_uses_template(client):
    """Letting detail returns 200 and uses lettings/letting.html."""
    address = Address.objects.create(
        number=22,
        street="Rue du Detail",
        city="Paris",
        state="FR",
        zip_code=75000,
        country_iso_code="FRA",
    )
    letting = Letting.objects.create(title="Detail Place", address=address)

    url = reverse("lettings:letting", kwargs={"letting_id": letting.id})
    response = client.get(url)

    assert response.status_code == 200
    assert "lettings/letting.html" in [t.name for t in response.templates]
    assert b"Detail Place" in response.content
