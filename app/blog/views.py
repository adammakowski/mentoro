from .models import Post, Category
# from accounts.models import Public
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import CommentForm, BlogForm
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.cache import cache_page


# @cache_page(60 * 5) # cache 60s * 5 = 5 minutes
def post_list(request):
    posts = Post.objects.filter(status=1, active=True).order_by('-created_date')
    categories = Category.objects.all()
    context = {'posts': posts, 'categories': categories}
    return render(request, 'blog_all.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    categories = Category.objects.filter(post=post)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            new_comment.name = request.user
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
            return redirect('blog_comment_success')
    else:
        comment_form = CommentForm()
    context = {'post': post, 'categories': categories, 'comments': comments, 'new_comment': new_comment, 'comment_form': comment_form}
    return render(request, 'blog_detail.html', context)


@login_required
def post_new(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('mentors_new_success')
    else:
        form = BlogForm()
    return render(request, 'blog_edit.html', {'form': form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            course = form.save(commit=False)
            course.author = request.user
            course.published_date = timezone.now()
            course.save()
            return redirect('blog_detail', pk=post.pk)
    else:
        form = BlogForm(instance=post)
    return render(request, 'blog_edit.html', {'form': form})


def category_list(request):
    categories = Category.objects.all()  # this will get all categories, you can do some filtering if you need (e.g. excluding categories without posts in it)
    context = {'categories': categories}
    return render(request, 'blog_categories.html', context)  # blog/category_list.html should be the template that categories are listed.


def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    posts = Post.objects.filter(status=1).order_by('-created_date')
    posts = posts.filter(category=category)
    context = {'posts': posts, 'category': category}
    return render(request, 'blog_category_detail.html', context)  # in this template, you will have access to category and posts under that category by (category.post_set).


def blog_comment_success(request):
    return render(request, 'blog_comment_success.html', {})
