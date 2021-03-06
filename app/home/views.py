from django.shortcuts import render
from .models import TermsMentor
from django.views.decorators.cache import cache_page

# Create your views here.

# @cache_page(60 * 5) # Cache time to live is 5 minutes.
def home_index(request):
    return render(request, 'home_index.html', {})


# @cache_page(60 * 60) # Cache time to live is 60 minutes.
def home_pricing(request):
    return render(request, 'home_pricing.html', {})


# @cache_page(60 * 15) # Cache time to live is 15 minutes.
def home_courses(request):
    return render(request, 'home_courses.html', {})


# @cache_page(60 * 15) # Cache time to live is 15 minutes.
def home_aboutus(request):
    return render(request, 'home_aboutus.html', {})


# @cache_page(60 * 15) # Cache time to live is 15 minutes.
def home_salescharges(request):
    return render(request, 'home_salescharges.html', {})


# @cache_page(60 * 60) # Cache time to live is 15 minutes.
def home_affiliate(request):
    return render(request, 'home_affiliate.html', {})


# @cache_page(60 * 60) # Cache time to live is 15 minutes.
def home_support(request):
    return render(request, 'home_support.html', {})


# @cache_page(60 * 60) # Cache time to live is 15 minutes.
def home_privacypolicy(request):
    return render(request, 'home_privacypolicy.html', {})

@cache_page(60 * 60) # Cache time to live is 60 minutes.
def mentors_instructions_and_regulations(request):
    terms_mentor = TermsMentor.objects.all
    return render(request, 'terms/mentors_instructions_and_regulations.html', {'terms_mentor': terms_mentor})
