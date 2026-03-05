# oc_lettings_site/urls.py

"""
Root URL configuration for the Django project.

This module defines the main URL routing for the application and
delegates URL handling to the corresponding apps using Django's
include mechanism.
"""

from django.contrib import admin
from django.urls import include
from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("lettings/", include("lettings.urls", namespace="lettings")),
    path("profiles/", include("profiles.urls", namespace="profiles")),
    path("admin/", admin.site.urls),
]