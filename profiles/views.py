# profiles/views.py
"""
Views for the profiles application.

Contains endpoints for listing profiles and showing a profile detail.
"""

from django.shortcuts import get_object_or_404
from django.shortcuts import render

from profiles.models import Profile


def index(request):
    """
    Render the profiles list page.

    Args:
        request (HttpRequest): Incoming HTTP request.

    Returns:
        HttpResponse: Rendered profiles index page.
    """
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """
    Render a profile detail page.

    Args:
        request (HttpRequest): Incoming HTTP request.
        username (str): Username to lookup.

    Returns:
        HttpResponse: Rendered profile detail page.
    """
    profile_obj = get_object_or_404(Profile, user__username=username)
    context = {"profile": profile_obj}
    return render(request, "profiles/profile.html", context)
