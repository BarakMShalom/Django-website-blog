"""
Admin configuration for the users app.

This module registers the Profile model with the Django admin interface.
"""

from django.contrib import admin
from .models import Profile

admin.site.register(Profile)
