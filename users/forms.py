"""
Forms for the users app.

This module defines the following forms:
- UserRegisterForm: Extends Django's UserCreationForm, adding an email field.
- UserUpdateForm: Extends Django's ModelForm for User, allowing updates to username and email.
- ProfileUpdateForm: Extends Django's ModelForm for Profile, allowing updates to the profile image.

Classes:
    UserRegisterForm: Form for user registration.
    UserUpdateForm: Form for updating user information.
    ProfileUpdateForm: Form for updating user profile information.
"""


from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
