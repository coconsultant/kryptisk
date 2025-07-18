# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("apps.authentication.urls")), # Auth routes - login / register
    path('accounts/', include('allauth.urls')),  # Allauth routes

    # ADD NEW Routes HERE
    path('notifications/', include('apps.notifications.urls')),

    # Leave `Home.Urls` as last the last line
    path("", include("apps.home.urls"))
]

if settings.DEBUG:
    urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + urlpatterns
