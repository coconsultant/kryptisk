# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class CustomUser(AbstractUser):
    bio = models.TextField(default='This is my bio.')
    registered_at = models.DateField(auto_now_add=True)
    social_twitter = models.URLField(default='')
    social_facebook = models.URLField(default='')
    social_instagram = models.URLField(default='')
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)


class TrackedEmail(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tracked_emails')
    email = models.EmailField()
    nickname = models.CharField(max_length=100, blank=True)
    is_verified = models.BooleanField(default=False)
    verification_token = models.CharField(max_length=100, blank=True, null=True, unique=True)

    class Meta:
        unique_together = ('user', 'email')

    def __str__(self):
        return f"{self.nickname} ({self.email})" if self.nickname else self.email

