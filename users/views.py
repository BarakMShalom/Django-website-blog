"""
Views for the users app.

This module defines views for user-related actions, such as registration and profile management.

Functions:
    register: View for handling user registration.
    profile: View for managing user profiles.

"""


from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    """
    View for handling user registration.

    If the request method is POST and the registration form is valid, a new user account is created,
    and the user is redirected to the login page with a success message.

    If the request method is GET, the registration form is displayed.

    Args:
        request: The HTTP request.

    Returns:
        HttpResponse: Rendered registration page or a redirect to the login page.
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}. Please Log in")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {'form': form})


@login_required
def profile(request):
    """
    View for managing user profiles.

    If the request method is POST and both the user update form and profile update form are valid,
    the user and profile information are updated, and a success message is displayed.

    If the request method is GET, the user and profile update forms are displayed.

    Args:
        request: The HTTP request.

    Returns:
        HttpResponse: Rendered profile page or a redirect to the profile page.
    """

    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        profile_update_form = ProfileUpdateForm(request.POST,
                                                request.FILES,
                                                instance=request.user.profile)
        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()
            messages.success(request, f"Your account has been updated.")
            return redirect('profile')

    else:
        user_update_form = UserUpdateForm(instance=request.user)
        profile_update_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': user_update_form,
        'p_form': profile_update_form
    }

    return render(request, 'users/profile.html', context)
