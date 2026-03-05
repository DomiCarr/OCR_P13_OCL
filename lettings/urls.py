# lettings/urls.py
"""
URL configuration for the lettings application.

Defines routes for listing lettings and displaying a single letting.
"""

from django.urls import path

from lettings import views

app_name = "lettings"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:letting_id>/", views.letting, name="letting"),
]
