from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy


def blog_home(request):
    """
    View for rendering the home page of the blog.

    Parameters:
    - request: HttpRequest object

    Returns:
    - HttpResponse object
    """
    context = {
        "posts": Post.objects.all()
    }
    return render(request, "blog/home.html", context)


class PostListView(ListView):
    """
    View for displaying a list of blog posts.

    Attributes:
    - model: The model to use for retrieving data (Post).
    - template_name: The template to render.
    - context_object_name: The variable name for the list in the template.
    - ordering: The ordering of the posts by date_posted.
    - paginate_by: Number of posts to display per page.
    """
    model = Post
    template_name = "blog/home.html"
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    """
    View for displaying a list of blog posts by a specific user.

    Attributes:
    - model: The model to use for retrieving data (Post).
    - template_name: The template to render.
    - context_object_name: The variable name for the list in the template.
    - ordering: The ordering of the posts by date_posted.
    - paginate_by: Number of posts to display per page.
    """
    model = Post
    template_name = "blog/user_posts.html"
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        """
        Get the queryset of posts for a specific user.

        Returns:
        - QuerySet of Post objects
        """
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    """
    View for displaying details of a single blog post.

    Attributes:
    - model: The model to use for retrieving data (Post).
    """
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    """
    View for creating a new blog post.

    Attributes:
    - model: The model to use for creating data (Post).
    - fields: The fields to include in the form.
    """
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        """
        Validate the form and set the author before saving.

        Parameters:
        - form: The form instance to validate.

        Returns:
        - HttpResponse object
        """
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    View for updating an existing blog post.

    Attributes:
    - model: The model to use for updating data (Post).
    - fields: The fields to include in the form.
    """
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        """
        Validate the form and set the author before saving.

        Parameters:
        - form: The form instance to validate.

        Returns:
        - HttpResponse object
        """
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """
        Check if the current user is the author of the post.

        Returns:
        - Boolean indicating whether the user passes the test.
        """
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    View for deleting an existing blog post.

    Attributes:
    - model: The model to use for deleting data (Post).
    - success_url: The URL to redirect to after successful deletion.
    """
    model = Post
    success_url = reverse_lazy('blog-home')

    def test_func(self):
        """
        Check if the current user is the author of the post.

        Returns:
        - Boolean indicating whether the user passes the test.
        """
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def blog_about(request):
    """
    View for rendering the about page of the blog.

    Parameters:
    - request: HttpRequest object

    Returns:
    - HttpResponse object
    """

    return render(request, "blog/about.html", {"title": "About"})
