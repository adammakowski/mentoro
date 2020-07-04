from django.shortcuts import render
from django.views.decorators.cache import cache_page
# Create your views here.

#@cache_page(60 * 60) # Cache time to live is 60 minutes.
def home_index(request):
    return render(request, 'home_index.html', {})
#@cache_page(60 * 60) # Cache time to live is 60 minutes.
def home_pricing(request):
    return render(request, 'home_pricing.html', {})
# @cache_page(60 * 15) # Cache time to live is 15 minutes.
def home_courses(request):
    return render(request, 'home_courses.html', {})
# @cache_page(60 * 15) # Cache time to live is 15 minutes.
def home_aboutus(request):
    return render(request, 'home_aboutus.html', {})
#@cache_page(60 * 15) # Cache time to live is 15 minutes.
def home_salescharges(request):
    return render(request, 'home_salescharges.html', {})
#@cache_page(60 * 60) # Cache time to live is 15 minutes.
def home_affiliate(request):
    return render(request, 'home_affiliate.html', {})