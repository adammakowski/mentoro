from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from django.shortcuts import render, get_object_or_404, redirect
from .models import Public
from .forms import PublicForm
from blog.models import Post, Category


def account_signup(request):
    if request.user.is_authenticated:
        return redirect('account_dashboard')
    else:
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


@cache_page(60 * 15)  # cache 60s * 5 = 15 minutes
def account_locked(request):
    return render(request, 'account_locked.html', {})


def public_detail(request, pk):
    profiles = get_object_or_404(Public, pk=pk, active=True)
    context = {'profiles': profiles}
    return render(request, 'public_profile_detail.html', context)  # in this template, you will have access to category and posts under that category by (category.post_set).


@login_required
def public_profile_edit(request, pk):
    profiles = get_object_or_404(Public, pk=pk)
    if request.user == profiles.user:
        if request.method == "POST":
            form = PublicForm(request.POST, instance=profiles)
            if form.is_valid():
                public = form.save(commit=False)
                public.user = request.user
                public.save()
                return redirect('public_detail', pk=public.pk)
        else:
            form = PublicForm(instance=profiles)
        return render(request, 'public_profile_edit.html', {'form': form})
    else:
        return redirect('home_index')


@login_required
def account_dashboard(request):
    return render(request, 'account_dashboard.html', {})


@login_required
def account_my_blog(request):
    posts = Post.objects.order_by('-created_date').filter(author=request.user)
    categories = Category.objects.all()
    context = {'posts': posts, 'categories': categories}
    return render(request, 'account_my_blog.html', context)
