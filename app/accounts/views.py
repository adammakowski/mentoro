from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from django.shortcuts import render, get_object_or_404, redirect
from .models import Public

def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Twoje konto zostało pomyślnie utworzone. Możesz się teraz zalogować.')
            return redirect('account_login')
    else:
        form = UserRegisterForm()
    return render(request, 'account_signup.html', {'form': form})


@login_required
def accounts_index(request):
    return render(request, 'account_index.html', {})

@cache_page(60 * 5) # cache 60s * 5 = 5 minutes
def account_locked(request):
    return render(request, 'account_locked.html', {})

def public(request):
    profiles = Public.objects.filter(active=True)
    return render(request, 'public_profile.html', {'profiles': profiles})
