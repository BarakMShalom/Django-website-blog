"""
Models for the users app.

This module defines the following model:
- Profile: Extends Django's Model for user profiles, including user information and profile image.

Classes:
    Profile: Model representing user profiles, linked to the built-in User model.

Methods:
    __str__: Human-readable representation of the Profile instance.
    save: Overrides the save method to resize and save the profile image if needed.
"""


from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    """
    Model representing user profiles.

    Fields:
        user: One-to-One relationship with the built-in User model.
        image: ImageField for the user's profile picture.

    Methods:
        __str__: Returns a human-readable representation of the profile.
        save: Overrides the save method to resize and save the profile image if needed.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        """Return a human-readable representation of the profile."""
        return f"{self.user.username} profile"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        """
        Override the save method to resize and save the profile image if needed.

        Args:
            force_insert: A boolean indicating whether to force an insert.
            force_update: A boolean indicating whether to force an update.
            using: The database alias to use.
            update_fields: The fields to update.

        Returns:
            None
        """
        super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
