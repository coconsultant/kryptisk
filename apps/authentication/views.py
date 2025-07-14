# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
import json
import os
import time # Import for time.time_ns()
import hashlib
import requests
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile
from django.contrib.auth import get_user_model # Import for explicitly refreshing user object

from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError
from .forms import LoginForm, SignUpForm, ProfileForm, TrackedEmailForm
from .models import TrackedEmail
from apps import Utils
from core.settings import *
from allauth.account.utils import send_email_confirmation


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
            # Save the user but set them as inactive
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            # Send email confirmation using allauth helper
            send_email_confirmation(request, user, signup=True)

            msg = 'User created successfully. Please check your email to verify your account.'
            success = True

            # Redirect to a page informing the user to check their email
            return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})


def profile(request):
    # GET request handler
    if request.method == 'GET':
        cache_buster = time.time_ns() # Get nanosecond precision for aggressive cache busting
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
            'cache_buster': cache_buster, # Pass the nanosecond timestamp to the template
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

    if action == 'upload_avatar':
        # Store the current avatar's FieldFile object *before* any updates
        old_avatar = request.user.avatar if request.user.avatar else None

        form = ProfileForm(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
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

                request.user.avatar = InMemoryUploadedFile(
                    output,
                    'ImageField',
                    avatar_file.name,
                    f'image/{img_format.lower()}',
                    output.getbuffer().nbytes,
                    None
                )

            request.user.save()

            # Delete the old avatar file after the new one has been successfully saved
            if old_avatar and old_avatar.name and old_avatar.storage.exists(old_avatar.name):
                try:
                    old_avatar.delete(save=False)
                except Exception as e:
                    print(f"Error deleting old avatar file '{old_avatar.name}': {e}") # Debug message

            return HttpResponseRedirect(request.path)

        return JsonResponse({
            'message': form.errors
        }, status=400)

    if action == 'use_gravatar':
        if not request.user.email:
            return JsonResponse({'message': 'No email associated with your account to fetch Gravatar. Please add an email address to use this feature.'}, status=400)

        # Store the current avatar's FieldFile object *before* any updates
        old_avatar = request.user.avatar if request.user.avatar else None

        email_hash = hashlib.md5(request.user.email.lower().strip().encode('utf-8')).hexdigest()
        # requesting size 800 to ensure good quality if resized
        gravatar_url = f"https://www.gravatar.com/avatar/{email_hash}?d=identicon&s=800"

        try:
            response = requests.get(gravatar_url, stream=True)
            response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)

            img = Image.open(BytesIO(response.content))

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

            gravatar_filename = f"gravatar_{request.user.username}.{img_format.lower()}"
            request.user.avatar = InMemoryUploadedFile(
                output,
                'ImageField',
                gravatar_filename,
                f'image/{img_format.lower()}',
                output.getbuffer().nbytes,
                None
            )
            request.user.save()

            # Delete the old avatar file after the new one has been successfully saved
            if old_avatar and old_avatar.name and old_avatar.storage.exists(old_avatar.name):
                try:
                    old_avatar.delete(save=False)
                except Exception as e:
                    print(f"Error deleting old avatar file '{old_avatar.name}': {e}") # Debug message

            return HttpResponseRedirect(request.path)

        except requests.exceptions.RequestException as e:
            return JsonResponse({'message': f'Error fetching Gravatar: {e}'}, status=500)
        except Exception as e:
            return JsonResponse({'message': f'Error processing Gravatar image: {e}'}, status=500)

    if action == 'reset_avatar':
        if request.user.avatar:
            # Delete the file from the filesystem if it exists
            if request.user.avatar.name and request.user.avatar.storage.exists(request.user.avatar.name):
                try:
                    request.user.avatar.delete(save=False)
                except Exception as e:
                    print(f"Error deleting avatar file '{request.user.avatar.name}': {e}")
            # Clear the avatar field in the database
            request.user.avatar = None
            request.user.save()

            # Refresh the user object from the database
            request.user.refresh_from_db()
            
        return HttpResponseRedirect(request.path)

    if action == 'update_name':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)

        return JsonResponse({
            'message': form.errors
        }, status=400)

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


@login_required(login_url="/login/")
def email_registration_view(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'add_email':
            tracked_emails = TrackedEmail.objects.filter(user=request.user)
            if tracked_emails.count() >= 2:
                messages.error(request, 'You can only have up to 2 tracked emails.')
                return redirect('email_registration')
            
            form = TrackedEmailForm(request.POST)
            if form.is_valid():
                email_to_track = form.cleaned_data['email']
                if email_to_track == request.user.email:
                    messages.error(request, 'You cannot track your primary email address.')
                else:
                    try:
                        tracked_email = form.save(commit=False)
                        tracked_email.user = request.user
                        tracked_email.save()
                        messages.success(request, 'Email address added successfully.')
                    except IntegrityError:
                        messages.error(request, 'This email address is already being tracked.')
            else:
                messages.error(request, 'Please correct the errors below.')

            return redirect('email_registration')
        
        elif action == 'edit_email':
            email_id = request.POST.get('email_id')
            try:
                tracked_email = TrackedEmail.objects.get(id=email_id, user=request.user)
                form = TrackedEmailForm(request.POST, instance=tracked_email)
                if form.is_valid():
                    new_email = form.cleaned_data['email']
                    if new_email == request.user.email:
                        messages.error(request, 'You cannot track your primary email address.')
                    else:
                        form.save()
                        messages.success(request, 'Email details updated successfully.')
                else:
                    messages.error(request, 'Update failed. Please check the details.')
            except TrackedEmail.DoesNotExist:
                messages.error(request, 'Email not found.')
            except IntegrityError:
                messages.error(request, 'This email address is already being tracked.')
            return redirect('email_registration')

        elif action == 'remove_email':
            email_id = request.POST.get('email_id')
            try:
                tracked_email = TrackedEmail.objects.get(id=email_id, user=request.user)
                tracked_email.delete()
                messages.success(request, 'Email address removed successfully.')
            except TrackedEmail.DoesNotExist:
                messages.error(request, 'Email not found.')
            return redirect('email_registration')

    # Calculate tracked emails and count after all POST operations
    tracked_emails = TrackedEmail.objects.filter(user=request.user)
    tracked_emails_count = tracked_emails.count()
    form = TrackedEmailForm()
    
    context = {
        'tracked_emails': tracked_emails,
        'tracked_emails_count': tracked_emails_count,
        'form': form,
        'segment': 'email-registration'
    }
    return render(request, 'accounts/email-registration.html', context)
