# oc_lettings_site/views.py
"""
Project-level views.

This module keeps only the homepage view of the site.
Feature-specific views are implemented inside their respective apps.
"""

from django.shortcuts import render


def index(request):
    """
    Render the site homepage.

    Args:
        request (HttpRequest): Incoming HTTP request.

    Returns:
        HttpResponse: Rendered homepage.
    """
    return render(request, "index.html")