# lettings/views.py
"""
Views for the lettings application.

Contains endpoints for listing lettings and showing a letting detail.
"""

import logging

from django.shortcuts import get_object_or_404
from django.shortcuts import render

from lettings.models import Letting

logger = logging.getLogger(__name__)


def index(request):
    """
    Render the lettings list page.

    Args:
        request (HttpRequest): Incoming HTTP request.

    Returns:
        HttpResponse: Rendered lettings index page.
    """
    lettings_list = Letting.objects.all()
    logger.info(
        "Lettings index accessed: lettings_count=%s path=%s method=%s",
        lettings_list.count(),
        request.path,
        request.method,
    )
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


def letting(request, letting_id):
    """
    Render a letting detail page.

    Args:
        request (HttpRequest): Incoming HTTP request.
        letting_id (int): Letting identifier.

    Returns:
        HttpResponse: Rendered letting detail page.
    """
    letting_obj = get_object_or_404(Letting, id=letting_id)
    logger.info(
        "Letting detail accessed: letting_id=%s title=%s path=%s method=%s",
        letting_id,
        letting_obj.title,
        request.path,
        request.method,
    )
    context = {
        "title": letting_obj.title,
        "address": letting_obj.address,
    }
    return render(request, "lettings/letting.html", context)
