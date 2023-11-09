from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    Configuration class for the 'blog' app.

    Attributes:
        default_auto_field (str): The default auto-generated field for models.
        name (str): The name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
