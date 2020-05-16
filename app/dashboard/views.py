from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

# @cache_page(60 * 1) # Cache time to live is 1 minutes.
@login_required
def dashboard_index(request):
    return render(request, 'dashboard_index.html', {})
