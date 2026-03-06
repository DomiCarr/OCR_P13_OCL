# oc_lettings_site/tests/test_errors.py
"""
Error page tests (404 and 500).

These are smoke tests ensuring the custom templates are used.
"""

import pytest
from django.test import override_settings
from django.urls import include, path
from django.test import Client

from oc_lettings_site import views


def boom(_request):
    """A view that raises to force a 500 error."""
    raise RuntimeError("Boom")


# Local URLConf for this test module (used via override_settings)
# IMPORTANT: include the same named routes used by base.html (index/lettings/profiles)
urlpatterns = [
    path("", views.index, name="index"),
    path("lettings/", include(("lettings.urls", "lettings"), namespace="lettings")),
    path("profiles/", include(("profiles.urls", "profiles"), namespace="profiles")),
    path("boom/", boom, name="boom"),
]

# Ensure Django uses the standard server_error handler that renders 500.html
handler500 = "django.views.defaults.server_error"


@pytest.mark.django_db
@override_settings(DEBUG=False)
def test_custom_404_template_used(client):
    """Unknown URL returns 404 and renders 404.html when DEBUG=False."""
    response = client.get("/this-page-does-not-exist/")
    assert response.status_code == 404
    assert "404.html" in [t.name for t in response.templates]


@pytest.mark.django_db
@override_settings(DEBUG=False, DEBUG_PROPAGATE_EXCEPTIONS=False, ROOT_URLCONF=__name__)
def test_custom_500_template_used():
    client = Client(raise_request_exception=False)
    response = client.get("/boom/")
    assert response.status_code == 500
    assert "500.html" in [t.name for t in response.templates]
