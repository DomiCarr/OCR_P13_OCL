# profiles/urls.py
"""
URL configuration for the profiles application.

Defines routes for listing profiles and displaying a single profile.
"""

from django.urls import path

from profiles import views

app_name = "profiles"

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:username>/", views.profile, name="profile"),
]