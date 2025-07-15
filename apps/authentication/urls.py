# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, include
from .views import login_view, register_user, profile, delete_account, email_registration_view, verify_tracked_email
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('profile/', profile, name="profile"),
    path('email-registration/', email_registration_view, name='email_registration'),
    path('verify-tracked-email/<str:token>/', verify_tracked_email, name='verify_tracked_email'),
    path('delete_account/', delete_account, name="delete-account"),
]
