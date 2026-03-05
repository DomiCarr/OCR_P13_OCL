# lettings/admin.py
"""
Admin configuration for the lettings application.

Registers the Address and Letting models so they can be managed
through the Django administration interface.
"""

from django.contrib import admin

from lettings.models import Address
from lettings.models import Letting


admin.site.register(Address)
admin.site.register(Letting)