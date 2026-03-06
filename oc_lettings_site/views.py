# oc_lettings_site/views.py
"""
Project-level views.

This module keeps only the homepage view of the site.
Feature-specific views are implemented inside their respective apps.
"""

import logging
from django.shortcuts import render


logger = logging.getLogger(__name__)


def index(request):
    """
    Render the site homepage and log access information.

    Args:
        request (HttpRequest): Incoming HTTP request.

    Returns:
        HttpResponse: Rendered homepage.
    """
    client_ip = request.META.get("REMOTE_ADDR")
    path = request.path
    method = request.method
    user = request.user if request.user.is_authenticated else "anonymous"

    logger.info(
        "Homepage accessed | ip=%s | path=%s | method=%s | user=%s",
        client_ip,
        path,
        method,
        user,
    )

    logger.error(
        "Sentry log test | ip=%s | path=%s | method=%s | user=%s",
        client_ip,
        path,
        method,
        user,
    )

    return render(request, "index.html")
