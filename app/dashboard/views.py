from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from accounts.models import Public
# Create your views here.

@login_required
def dashboard_index(request):
    return render(request, 'dashboard_index.html', {})

@login_required
def dashboard_public_profile(request):
    profiles = Public.objects.filter(user= request.user)
    context = {'profiles': profiles}
    return render(request, 'dashboard_public_profile.html', context)

@login_required
def add_new(request):
    return render(request, 'add_new.html', {})
