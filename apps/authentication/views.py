# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
import json
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
        # Safely get avatar URL, providing a default if no avatar is set
        # This avatar_url is passed to context, though the template directly uses request.user.avatar.url
        avatar_url = request.user.avatar.url if request.user.avatar else f"{ASSETS_ROOT}/img/added-images/default.png"

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
            'avatar_url': avatar_url,
        })

    # POST request handler
    try:
        body = json.loads(request.body)
    except Exception as _:
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

    if action == 'edit_bio' or action == 'edit_social_link' or action == 'upload_avatar':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            user_profile = form.save(commit=False) # Get instance without saving to DB yet

            if 'avatar' in request.FILES and request.FILES['avatar']: # Check if avatar file was actually uploaded
                avatar_file = request.FILES['avatar']
                img = Image.open(avatar_file)

                # Resize image if larger than 800x800
                max_size = (800, 800)
                if img.width > max_size[0] or img.height > max_size[1]:
                    img.thumbnail(max_size, Image.LANCZOS)

                # Determine image format for saving
                img_format = img.format if img.format else 'PNG'
                if img_format not in ['JPEG', 'PNG', 'GIF', 'BMP', 'TIFF', 'WEBP']:
                    img_format = 'PNG' # Fallback to a common format

                # Convert to RGB if saving as JPEG from a transparent format
                if img_format == 'JPEG' and img.mode in ('RGBA', 'P'):
                    img = img.convert('RGB')
                
                output = BytesIO()
                # Save the processed image to a BytesIO object
                img.save(output, format=img_format, quality=85) # Add quality for JPEG
                output.seek(0)

                # Assign the processed image content to the avatar field
                # This replaces the original uploaded file content with the processed one.
                user_profile.avatar.save(
                    avatar_file.name, # Use original filename as a base
                    ContentFile(output.read()), # Pass the bytes from BytesIO
                    save=False # Do not save the model instance yet
                )

            user_profile.save() # Finally save the model instance and the avatar file (which has been updated)

            # Explicitly refresh the request.user object from the database
            # This ensures that when the page is re-rendered after redirect,
            # request.user.avatar.url contains the latest value.
            User = get_user_model()
            request.user = User.objects.get(pk=request.user.pk)

            # Redirect to the profile page after successful update
            return HttpResponseRedirect(request.path)

        # If form is not valid, return JSON response with errors
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
