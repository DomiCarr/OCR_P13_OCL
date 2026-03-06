# oc_lettings_site/tests/test_admin.py
"""
Admin tests.

Minimal checks that models are registered in the Django admin site.
"""

from django.contrib.admin.sites import site

from lettings.models import Address, Letting
from profiles.models import Profile


def test_models_registered_in_admin():
    """Address, Letting and Profile are registered in admin."""
    assert Address in site._registry
    assert Letting in site._registry
    assert Profile in site._registry
