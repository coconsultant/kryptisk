# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse


def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    
    # Handle avatar upload
    if request.method == 'POST' and request.POST.get('action') == 'upload_avatar':
        # This block is now handled by apps/authentication/views.py.
        # It's good practice to centralize such logic.
        # This part of the code might become redundant if all avatar logic moves to authentication app.
        # For now, I will leave it as is, however, it's worth noting that if the authentication.views.profile
        # is handling it, this block may lead to unexpected behavior if both are active paths.
        # If this is the "pages" view for general site pages and not directly for profile management,
        # it might be better to remove this block from here. Assuming profile view is primary.
        if 'avatar' in request.FILES:
            request.user.avatar = request.FILES['avatar']
            request.user.save()
            return HttpResponseRedirect(request.path)
    
    # Add bio to context
    if request.user.is_authenticated:
        context['bio'] = request.user.bio
    
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
