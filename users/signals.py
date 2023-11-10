"""
Signal handlers for the users app.

This module defines signal handlers for the User model, specifically for creating and saving user profiles.

Functions:
    create_profile: Signal handler for post_save event on User model to create a corresponding Profile instance.
    save_profile: Signal handler for post_save event on User model to save the associated Profile instance.

"""


from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Signal handler for post_save event on User model to create a corresponding Profile instance.

    Args:
        sender: The model class.
        instance: The actual instance being saved.
        created: A boolean indicating whether the instance was created.
        **kwargs: Additional keyword arguments.

    Returns:
        None: This function doesn't return anything explicitly.
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """
    Signal handler for post_save event on User model to save the associated Profile instance.

    Args:
        sender: The model class.
        instance: The actual instance being saved.
        **kwargs: Additional keyword arguments.

    Returns:
        None: This function doesn't return anything explicitly.
    """
    instance.profile.save()
