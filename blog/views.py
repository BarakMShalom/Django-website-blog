from django.shortcuts import render
from .models import Post


def blog_home(request):
    """
        Render the home page of the blog.

        Retrieves all blog posts from the database and displays them on the home page.

        Args:
            request: HttpRequest object representing the current request.

        Returns:
            Rendered HTML page displaying a list of blog posts.

    """
    context = {
        "posts": Post.objects.all()
    }
    return render(request, "blog/home.html", context)


def blog_about(request):
    """
        Render the 'About' page of the blog.

        Args:
            request: HttpRequest object representing the current request.

        Returns:
            Rendered HTML page with information about the blog.
    """
    return render(request, "blog/about.html", {"title": "About"})
