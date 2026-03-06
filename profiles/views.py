# profiles/views.py
"""
Views for the profiles application.

Contains endpoints for listing profiles and showing a profile detail.
"""

import logging

from django.shortcuts import get_object_or_404
from django.shortcuts import render

from profiles.models import Profile


logger = logging.getLogger(__name__)


def index(request):
    """
    Render the profiles list page.

    Args:
        request (HttpRequest): Incoming HTTP request.

    Returns:
        HttpResponse: Rendered profiles index page.
    """
    profiles_list = Profile.objects.all()

    logger.info(
        "Profiles index accessed | count=%s | path=%s | method=%s",
        profiles_list.count(),
        request.path,
        request.method,
    )

    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """
    Render a profile detail page.

    Args:
        request (HttpRequest): Incoming HTTP request.
        username (str): Username linked to the profile.

    Returns:
        HttpResponse: Rendered profile detail page.
    """
    profile_obj = get_object_or_404(Profile, user__username=username)

    logger.info(
        "Profile detail accessed | username=%s | favorite_city=%s | path=%s | method=%s",
        username,
        profile_obj.favorite_city,
        request.path,
        request.method,
    )

    context = {
        "profile": profile_obj,
    }
    return render(request, "profiles/profile.html", context)
