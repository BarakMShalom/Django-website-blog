from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_home, name="blog-home"),
    path("about/", views.blog_about, name="blog-about"),
]
