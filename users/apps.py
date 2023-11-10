"""
Configuration for the users app.

This module defines the UsersConfig class, which inherits from Django's AppConfig.
It specifies the default auto field and registers signals when the app is ready.

Attributes:
    default_auto_field (str): The default auto field for model definitions.
    name (str): The name of the app.

Methods:
    ready(): A method called when the app is ready. It imports and registers signals.
"""

from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        import users.signals
