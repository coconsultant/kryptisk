# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import (
    login_view, register_user, profile, delete_account, email_registration_view,
    verify_tracked_email # Added verify_tracked_email
)

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_user, name='register'),
    path('profile/', profile, name='profile'),
    path('delete-account/', delete_account, name='delete_account'),
    path('email-registration/', email_registration_view, name='email_registration'),
    path('verify-email/<str:token>/', verify_tracked_email, name='verify_tracked_email'), # New URL pattern
]
