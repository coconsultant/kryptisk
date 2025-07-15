# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
import json
import os
import time # Import for time.time_ns()
import hashlib
import uuid
import requests
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile
from django.contrib.auth import get_user_model # Import for explicitly refreshing user object

from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404 # Added get_object_or_404
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError
from .forms import LoginForm, SignUpForm, ProfileForm, TrackedEmailForm
from .models import TrackedEmail
from apps.notifications.models import Notification
from apps import Utils
from core.settings import *
from allauth.account.models import EmailAddress
from datetime import timedelta # Import datetime for trial calculation
from django.utils import timezone # Import timezone for current date


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
            # Save the user as active since allauth will handle email verification
            user = form.save(commit=False)
            user.is_active = True
            user.save()

            # Send email confirmation using allauth helper
            if user.email:
                EmailAddress.objects.add_email(request, user, user.email, signup=True, confirm=True)

            # Create a welcome notification
            Notification.objects.create(user=user, message="Welcome to Kryptisk! We're glad to have you.")

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
    # Define trial duration
    TRIAL_DURATION_DAYS = 3

    # Calculate trial days left
    days_left = None
    if request.user.is_authenticated and request.user.registered_at:
        # Calculate days since registration
        today = timezone.now().date()
        days_since_registration = (today - request.user.registered_at).days
        
        # Calculate remaining trial days
        days_left = TRIAL_DURATION_DAYS - days_since_registration
        
        # Ensure days_left doesn't go below zero if trial expired
        if days_left < 0:
            days_left = 0

    # GET request handler
    if request.method == 'GET':
        cache_buster = time.time_ns() # Get nanosecond precision for aggressive cache busting
        return render(request, "accounts/user-profile.html", context={
            'bio': request.user.bio,
            'registered_at': request.user.registered_at,
            'days_left_on_trial': days_left, # Pass days left to the template
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
            return JsonResponse({
                'message': 'Profile updated successfully.'
            }, status=200)

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
    # Calculate non_primary_tracked_emails_count for template and add_email logic
    non_primary_tracked_emails_count = TrackedEmail.objects.filter(user=request.user).exclude(email=request.user.email).count()

    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'add_email':
            # `non_primary_tracked_emails_count` controls the limit for adding new emails
            form = TrackedEmailForm(request.POST)
            if form.is_valid():
                email_to_track = form.cleaned_data['email']
                
                if email_to_track == request.user.email:
                    Notification.objects.create(user=request.user, message='Your primary email is managed via the dedicated checkbox. Please add other email addresses here.')
                    return redirect('email_registration')
                elif non_primary_tracked_emails_count >= 2: # Changed to use non_primary_tracked_emails_count
                    Notification.objects.create(user=request.user, message='You have reached the maximum of 2 additional tracked emails. Please remove an existing email to add a new one.')
                    return redirect('email_registration')
                else:
                    try:
                        tracked_email = form.save(commit=False)
                        tracked_email.user = request.user
                        tracked_email.is_verified = False
                        tracked_email.verification_token = uuid.uuid4().hex
                        tracked_email.save()

                        # Send verification email
                        verification_link = request.build_absolute_uri(
                            reverse('verify_tracked_email', kwargs={'token': tracked_email.verification_token})
                        )
                        subject = 'Verify Your Email for Kryptisk Tracking'
                        message_body = f"Please click the link to verify your email address for tracking: {verification_link}"
                        send_mail(
                            subject,
                            message_body,
                            EMAIL_SENDER,
                            [tracked_email.email],
                            fail_silently=False,
                        )
                        
                        Notification.objects.create(user=request.user, message='Email address added. A verification email has been sent.')
                        return redirect('email_registration')
                    except IntegrityError:
                        Notification.objects.create(user=request.user, message='This email address is already being tracked for your account.')
                        return redirect('email_registration')
            else:
                # Form is invalid, it will be re-rendered with errors, so no generic notification is needed.
                pass

            # If we fall through, re-render the page with form errors
            tracked_emails = TrackedEmail.objects.filter(user=request.user)
            # is_primary_email_tracked is already calculated and used in context for GET request,
            # so it needs to be calculated again here to pass to the context for POST
            is_primary_email_tracked = TrackedEmail.objects.filter(user=request.user, email=request.user.email).exists()

            context = {
                'tracked_emails': tracked_emails,
                'non_primary_tracked_emails_count': non_primary_tracked_emails_count, # Pass for re-rendering form
                'form': form,
                'segment': 'email-registration',
                'is_primary_email_tracked': is_primary_email_tracked,
            }
            return render(request, 'accounts/email-registration.html', context)
        
        elif action == 'toggle_primary_email_tracking':
            primary_email = request.user.email
            track_primary = request.POST.get('track_primary_email_checkbox') == 'on' 
            
            primary_email_tracked_obj = TrackedEmail.objects.filter(user=request.user, email=primary_email).first()
            # This count (excluding primary) is correctly used for this specific action's limit check
            current_non_primary_tracked_emails_count_for_toggle = TrackedEmail.objects.filter(user=request.user).exclude(email=primary_email).count()

            if track_primary: # User wants to track primary email
                if not primary_email_tracked_obj: # If it's not already tracked
                    if current_non_primary_tracked_emails_count_for_toggle < 2: # Check if there's space for primary + 1 more (max 2 total, excluding potential primary which IS being added)
                        try:
                            # Create new TrackedEmail for primary email
                            TrackedEmail.objects.create(
                                user=request.user, 
                                email=primary_email, 
                                is_verified=True, # Primary email is implicitly verified
                                nickname='Primary Account Email' # Default nickname for primary email
                            )
                            Notification.objects.create(user=request.user, message='Your primary email is now being tracked.')
                        except IntegrityError:
                            Notification.objects.create(user=request.user, message='Your primary email is already tracked.')
                    else:
                        Notification.objects.create(user=request.user, message='You have reached the maximum of 2 additional tracked emails. Please untrack another email to track your primary email.')
                elif not primary_email_tracked_obj.is_verified:
                    # If it exists but wasn't verified (shouldn't happen for primary, but for robustness)
                    primary_email_tracked_obj.is_verified = True
                    primary_email_tracked_obj.verification_token = None
                    primary_email_tracked_obj.save()
                    Notification.objects.create(user=request.user, message='Your primary email is now being tracked and verified.')
                else:
                    Notification.objects.create(user=request.user, message='Your primary email is already being tracked.')
            else: # User wants to untrack primary email
                if primary_email_tracked_obj:
                    # It's important to only remove if it's the primary email object
                    # This prevents accidentally removing another tracked email if for some reason
                    # its email address matches the primary_email although it shouldn't be the case
                    # based on the unique_together constraint and current logic.
                    if primary_email_tracked_obj.email == primary_email:
                        primary_email_tracked_obj.delete()
                        Notification.objects.create(user=request.user, message='Your primary email is no longer being tracked.')
                else:
                    Notification.objects.create(user=request.user, message='Your primary email was not being tracked.')
            
            return redirect('email_registration')

        elif action == 'edit_email':
            email_id = request.POST.get('email_id')
            try:
                tracked_email = TrackedEmail.objects.get(id=email_id, user=request.user)
                original_email = tracked_email.email
                form = TrackedEmailForm(request.POST, instance=tracked_email)
                if form.is_valid():
                    new_email = form.cleaned_data['email']
                    if new_email == request.user.email and original_email != request.user.email:
                        Notification.objects.create(user=request.user, message='Your primary email is managed via the dedicated checkbox. You cannot set another tracked email to be your primary email through this edit function.')
                    elif TrackedEmail.objects.filter(user=request.user, email=new_email).exclude(id=tracked_email.id).exists():
                         Notification.objects.create(user=request.user, message='This email address is already being tracked for your account.')
                    else:
                        instance = form.save(commit=False)
                        if new_email != original_email:
                            instance.is_verified = False
                            instance.verification_token = uuid.uuid4().hex
                            
                            # Send verification email for the new address
                            verification_link = request.build_absolute_uri(
                                reverse('verify_tracked_email', kwargs={'token': instance.verification_token})
                            )
                            subject = 'Verify Your Email for Kryptisk Tracking'
                            message_body = f"Please click the link to verify your email address for tracking: {verification_link}"
                            send_mail(
                                subject,
                                message_body,
                                EMAIL_SENDER,
                                [new_email],
                                fail_silently=False,
                            )
                            Notification.objects.create(user=request.user, message='Email updated. A verification email has been sent to the new address.')
                        else:
                            Notification.objects.create(user=request.user, message='Email details updated successfully.')
                        
                        instance.save()
                else:
                    Notification.objects.create(user=request.user, message='Update failed. Please check the details.')
            except TrackedEmail.DoesNotExist:
                Notification.objects.create(user=request.user, message='Email not found.')
            except IntegrityError: 
                Notification.objects.create(user=request.user, message='This email address is already being tracked for your account.')
            return redirect('email_registration')

        elif action == 'remove_email':
            email_id = request.POST.get('email_id')
            try:
                tracked_email = TrackedEmail.objects.get(id=email_id, user=request.user)
                if tracked_email.email == request.user.email:
                    Notification.objects.create(user=request.user, message='You cannot remove your primary email directly. Please uncheck the "Track this email" box next to it.')
                else:
                    tracked_email.delete()
                    Notification.objects.create(user=request.user, message='Email address removed successfully.')
            except TrackedEmail.DoesNotExist:
                Notification.objects.create(user=request.user, message='Email not found.')
            return redirect('email_registration')

        elif action == 'resend_verification':
            email_id = request.POST.get('email_id')
            try:
                tracked_email = get_object_or_404(TrackedEmail, id=email_id, user=request.user)

                if tracked_email.is_verified:
                    Notification.objects.create(user=request.user, message=f'The email address {tracked_email.email} is already verified.')
                else:
                    # Generate a new verification token
                    tracked_email.verification_token = uuid.uuid4().hex
                    tracked_email.save()

                    # Send verification email with the new token
                    verification_link = request.build_absolute_uri(
                        reverse('verify_tracked_email', kwargs={'token': tracked_email.verification_token})
                    )
                    subject = 'Verify Your Email for Kryptisk Tracking'
                    message_body = f"Please click the link to verify your email address for tracking: {verification_link}"
                    send_mail(
                        subject,
                        message_body,
                        EMAIL_SENDER,
                        [tracked_email.email],
                        fail_silently=False,
                    )
                    Notification.objects.create(user=request.user, message=f'A new verification email has been sent to {tracked_email.email}. Please check your inbox.')

            except TrackedEmail.DoesNotExist:
                Notification.objects.create(user=request.user, message='Email not found or unauthorized.')
            except Exception as e:
                print(f'Error resending verification email: {e}') # For debugging
                Notification.objects.create(user=request.user, message='An error occurred while trying to resend the verification email.')

            return redirect('email_registration')

    # This is now for GET requests only
    tracked_emails = TrackedEmail.objects.filter(user=request.user)
    form = TrackedEmailForm()

    # Determine if primary email is currently tracked
    is_primary_email_tracked = TrackedEmail.objects.filter(user=request.user, email=request.user.email).exists()
    
    context = {
        'tracked_emails': tracked_emails,
        'non_primary_tracked_emails_count': non_primary_tracked_emails_count, # Pass this to template
        'form': form,
        'segment': 'email-registration',
        'is_primary_email_tracked': is_primary_email_tracked, # Pass this to template
    }
    return render(request, 'accounts/email-registration.html', context)


def verify_tracked_email(request, token):
    """
    View to handle email verification for tracked emails.
    """
    tracked_email = get_object_or_404(TrackedEmail, verification_token=token)

    if tracked_email.is_verified:
        Notification.objects.create(user=tracked_email.user, message=f'The email address {tracked_email.email} is already verified.')
    else:
        tracked_email.is_verified = True
        tracked_email.verification_token = None  # Clear the token after use
        tracked_email.save()
        Notification.objects.create(user=tracked_email.user, message=f'Your email address {tracked_email.email} has been successfully verified for tracking!')

    return redirect('email_registration')
