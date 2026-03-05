# lettings/models.py
"""
Models for the lettings application.

This module defines the database models used to represent rental
properties and their associated addresses.
"""

from django.db import models


class Address(models.Model):
    """Represents a physical address associated with a letting."""

    number = models.PositiveIntegerField()
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2)
    zip_code = models.PositiveIntegerField()
    country_iso_code = models.CharField(max_length=3)

    def __str__(self):
        """Return a readable representation of the address."""
        return f"{self.number} {self.street}"

    class Meta:
        """Model metadata."""

        verbose_name_plural = "Addresses"


class Letting(models.Model):
    """Represents a rental property."""

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """Return the title of the letting."""
        return self.title

    class Meta:
        """Model metadata."""

        verbose_name_plural = "Lettings"