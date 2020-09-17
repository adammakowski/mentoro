from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Public

@login_required
def accounts_index(request):
    return render(request, 'account_index.html', {})

@cache_page(60 * 5) # cache 60s * 5 = 5 minutes
def account_locked(request):
    return render(request, 'account_locked.html', {})

def public(request):
    profiles = Public.objects.filter(active=True)
    return render(request, 'public_profile.html', {'profiles': profiles})
