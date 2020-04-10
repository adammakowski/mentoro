from django.shortcuts import render
# Create your views here.

# @cache_page(60 * 1) # Cache time to live is 1 minutes.
def home_index(request):
    return render(request, 'home_index.html', {})
