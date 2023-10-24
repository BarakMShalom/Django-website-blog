from django.shortcuts import render
from .models import Post


def blog_home(request):
    context = {
        "posts": Post.objects.all()
    }
    return render(request, "blog/home.html", context)


def blog_about(request):
    return render(request, "blog/about.html", {"title": "About"})
