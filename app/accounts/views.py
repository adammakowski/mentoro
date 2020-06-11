from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

# @cache_page(60 * 1) # Cache time to live is 1 minutes.
@login_required
def accounts_index(request):
    return render(request, 'accounts_index.html', {})
