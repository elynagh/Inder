from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout
from django.conf import settings
from django.contrib.auth.decorators import login_required
import json
from . import models, forms
from django.contrib import messages

# Create your views here.
def reports(request):
    return render(request, 'inder_site/reports.html')

def splash(request):
    user = request.user
    if user.is_authenticated:
        if user.first_name is None or user.last_name is None or user.bio is None:
            return redirect(complete_profile)
        elif user.idea_generator and not user.has_idea():
            return render(request, 'inder_site/create_idea.html')
        else:
            return render(request, 'inder_site/splash.html')
    else:
        return render(request, 'inder_site/splash.html')
    

@login_required
def logout(request):
    django_logout(request)
    domain = settings.SOCIAL_AUTH_AUTH0_DOMAIN
    client_id = settings.SOCIAL_AUTH_AUTH0_KEY
    return_to = 'http://127.0.0.1:8000' # this can be current domain
    return redirect(f'https://{domain}/v2/logout?client_id={client_id}&returnTo={return_to}')

@login_required
def complete_profile(request):
    user = request.user
    name = user.first_name
    last = user.last_name
    email = user.email
    bio = user.bio
    show_last = user.show_last_name
    idea_gen = user.idea_generator
    collab = user.collaborator
    if request.method == 'POST':
        form = forms.UserProfileForm(request.POST)
        if form.is_valid:
            if request.POST['first_name'] != name:
                user.first_name = request.POST['first_name']
            else:
                user.name = name

            if request.POST['last_name'] != last:
                user.last_name = request.POST['last_name']
            else:
                user.last = last

            if request.POST['bio'] != bio:
                user.bio = request.POST['bio']
            else:
                user.bio = bio

            if request.POST.get('show_last_name'):
                user.show_last_name = True
            else:
                user.show_last_name = False

            if request.POST.get('idea_generator'):
                user.idea_generator = True
            else:
                user.idea_generator = False

            if request.POST.get('collaborator'):
                user.collaborator = True
            else:
                user.collaborator = False

            user.save()
            return redirect(splash)
    form = forms.UserProfileForm(instance=user)
    context = dict(form=form)
    return render(request, 'inder_site/complete_profile.html', context)

@login_required
def create_idea(request):
    user = request.user
    print(request.method)
    if request.method == 'POST':
        form = forms.CreateIdeaform(request.POST)
        if form.is_valid:
            models.Idea.objects.create(
                user=user,
                idea_title = request.POST['idea_name'],
                text = request.POST['description']
            )
            return redirect(splash)
    form = forms.CreateIdeaform()
    context = dict(form=form)
    return render(request, 'inder_site/create_idea.html', context)