"""
Admin configuration for the Blog app.

This file defines how the Post model should be displayed
and managed in the Django admin interface.
"""

from django.contrib import admin
from .models import Post

admin.site.register(Post)
