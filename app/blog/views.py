from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.cache import cache_page
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import BlogPost
from .forms import BlogForm
# Create your views here.

# cache_page(60 * 1) # Cache time to live is 15 minutes.
def blog_all(request):
    blog_post = BlogPost.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog_all.html', {'blog_post': blog_post})

# @cache_page(60 * 15) # Cache time to live is 15 minutes.
def blog_detail(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog_detail.html', {'blog_post': blog_post})

#@cache_page(60 * 15) # Cache time to live is 15 minutes.
@login_required
def blog_new(request):
    if request.method == "POST":
        form = BlogPost(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.published_date = timezone.now()
            blog_post.save()
            return redirect('blog_detail', pk=blog_post.pk)
    else:
        form = BlogPost()
    return render(request, 'blog_edit.html', {'form': form})

#@cache_page(60 * 15) # Cache time to live is 1 minutes.
@login_required
def blog_edit(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == "POST":
        form = BlogForm(request.POST, instance=post)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.published_date = timezone.now()
            blog_post.save()
            return redirect('blog_detail', pk=blog_post.pk)
    else:
        form = BlogForm(instance=post)
    return render(request, 'blog_edit.html', {'form': form})