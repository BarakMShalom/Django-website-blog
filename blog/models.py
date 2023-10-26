from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    """This module defines the database model for blog posts in the application.

    The `Post` model class is used to represent blog posts. It defines the structure
    of the `Post` table in the database.

    Attributes:
        title (CharField): A character field representing the post's title.
        content (TextField): A text field for the post's content.
        date_posted (DateTimeField): A date and time field for the post's creation date.
        author (ForeignKey): A foreign key relationship to the `User` model, which
            represents the author of the post. The `on_delete` parameter specifies
            the behavior when a related `User` instance is deleted.

    Methods:
        __str__(): A special method that returns a string representation of a `Post`
        instance, which is used when displaying a `Post` object in the admin panel
        and other contexts.

    Example:
        To create a new post, you can use the `Post` model like this:

        new_post = Post(title="Sample Post", content="This is the content of the post.")
        new_post.save()
    """
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
