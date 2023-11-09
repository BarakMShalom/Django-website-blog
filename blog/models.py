from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    """
    Model representing a blog post.

    Attributes:
        title (str): The title of the post.
        content (str): The content of the post.
        date_posted (datetime): The date and time when the post was created.
        author (User): The author of the post, linked to the User model.
    """

    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """String representation of the Post."""
        return self.title

    def get_absolute_url(self):
        """
        Returns the URL to access a detail record for this post.

        Returns:
            str: The URL of the post detail view.
        """
        return reverse('post-detail', kwargs={'pk': self.pk})
