# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
import json
import os
import time
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile
from django.contrib.auth import get_user_model # Import for explicitly refreshing user object

from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, SignUpForm, ProfileForm
from apps import Utils
from core.settings import *


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg,
                                                   "github_login": GITHUB_AUTH, "twitter_login": TWITTER_AUTH})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created successfully.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})


def profile(request):
    # GET request handler
    if request.method == 'GET':
        return render(request, "accounts/user-profile.html", context={
            'bio': request.user.bio,
            'registered_at': request.user.registered_at,
            'contact_us_info': {
                'phone': SITE_OWNER_PHONE,
                'email': SITE_OWNER_MAIL,
                'address': SITE_OWNER_ADDRESS,
                'facebook': SITE_OWNER_FBK,
                'twitter': SITE_OWNER_TWITTER,
                'instagram': SITE_OWNER_INSTAGRAM,
            },
            # 'debug' is automatically available in templates when DEBUG=True in settings.py
            # via django.template.context_processors.debug if configured in TEMPLATES options.
        })

    # POST request handler
    if 'multipart/form-data' in request.content_type:
        body = request.POST
    else:
        try:
            body = json.loads(request.body)
        except Exception:
            body = request.POST

    action = body.get('action')

    if action == 'contact_us':

        subject = body.get('subject')
        email = body.get('email', request.user.email)
        message = body.get('message')
        name = body.get('name')

        try:
            send_mail(subject, f'sender: {request.user} - {name} - {email} \nmessage: \n{message}',
                      EMAIL_SENDER, [SITE_OWNER_MAIL])
        except Exception as e:

            print(f'There is an error in sending email: {str(e)}')
            return JsonResponse({
                'message': 'Error sending email. Please review settings.'
            }, status=400)

        return JsonResponse({
            'message': 'message successfully sent.'
        }, status=200)

    if action == 'upload_avatar': # Re-evaluate this action if it needs form validation
        form = ProfileForm(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            user_profile = form.save(commit=False) 

            if 'avatar' in request.FILES and request.FILES['avatar']:
                avatar_file = request.FILES['avatar']
                img = Image.open(avatar_file)

                max_size = (800, 800)
                if img.width > max_size[0] or img.height > max_size[1]:
                    img.thumbnail(max_size, Image.LANCZOS)

                img_format = img.format if img.format else 'PNG'
                if img_format.upper() not in ['JPEG', 'PNG', 'GIF', 'BMP', 'TIFF', 'WEBP']:
                    img_format = 'PNG'

                if img_format.upper() == 'JPEG' and img.mode in ('RGBA', 'P'):
                    img = img.convert('RGB')

                output = BytesIO()
                img.save(output, format=img_format, quality=85)
                output.seek(0)

                user_profile.avatar = InMemoryUploadedFile(
                    output,
                    'ImageField',
                    avatar_file.name,
                    f'image/{img_format.lower()}',
                    output.getbuffer().nbytes,
                    None
                )

            user_profile.save()

            User = get_user_model()
            updated_user = User.objects.get(pk=request.user.pk)
            
            for attr in ['avatar', 'bio', 'social_twitter', 'social_facebook', 'social_instagram']:
                setattr(request.user, attr, getattr(updated_user, attr))

            return HttpResponseRedirect(request.path)

        return JsonResponse({
            'message': form.errors
        }, status=400)

    if action == 'reset_avatar':
        if request.user.avatar:
            # Delete the file from the filesystem if it exists
            if os.path.exists(request.user.avatar.path):
                os.remove(request.user.avatar.path)
            # Clear the avatar field in the database
            request.user.avatar = None
            request.user.save()

            # Explicitly refresh the request.user object from the database
            User = get_user_model()
            updated_user = User.objects.get(pk=request.user.pk)
            setattr(request.user, 'avatar', getattr(updated_user, 'avatar'))
            
        return HttpResponseRedirect(request.path)

    if action == 'edit_bio' or action == 'edit_social_link': # This part was already present, keeping for full context
        form = ProfileForm(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)

        return JsonResponse({
            'message': form.errors
        }, status=400)


def delete_account(request):
    result, message = Utils.delete_user(request.user.username)
    if not result:
        return JsonResponse({
            'errors': message
        }, status=400)
    logout(request)
    return HttpResponseRedirect('/')
