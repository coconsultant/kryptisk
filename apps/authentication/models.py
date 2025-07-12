# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    bio = models.TextField(default='This is my bio.')
    registered_at = models.DateField(auto_now=True)
    social_twitter = models.URLField(default='')
    social_facebook = models.URLField(default='')
    social_instagram = models.URLField(default='')
