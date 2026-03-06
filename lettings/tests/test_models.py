# lettings/tests/test_models.py
"""
Model tests for the lettings application.

These tests focus on custom behavior (e.g., __str__) without over-testing
Django's ORM.
"""

import pytest

from lettings.models import Address, Letting


@pytest.mark.django_db
def test_address_str():
    """Address.__str__ returns a readable address."""
    address = Address.objects.create(
        number=123,
        street="Main Street",
        city="Paris",
        state="FR",
        zip_code=75000,
        country_iso_code="FRA",
    )
    assert str(address) == "123 Main Street"


@pytest.mark.django_db
def test_letting_str():
    """Letting.__str__ returns the letting title."""
    address = Address.objects.create(
        number=1,
        street="Rue de Test",
        city="Paris",
        state="FR",
        zip_code=75000,
        country_iso_code="FRA",
    )
    letting = Letting.objects.create(title="Cozy Flat", address=address)
    assert str(letting) == "Cozy Flat"
