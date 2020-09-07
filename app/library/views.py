from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.decorators.cache import cache_page
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Library
from .forms import LibraryForm
# Create your views here.

# cache_page(60 * 1) # Cache time to live is 15 minutes.
class LibraryList(generic.ListView):
    queryset = Library.objects.filter(status=1).order_by('-created_date')
    template_name = 'library_all.html'
    paginate_by = 3

#@cache_page(60 * 5) # cache 60s * 5 = 5 minutes
def library_detail(request, slug):
    template_name = 'blog_detail.html'
    post = get_object_or_404(Library, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = LibraryForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            new_comment.name = request.user
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = LibraryForm()

    return render(request, template_name, {'post': post, 'comments': comments, 'new_comment': new_comment, 'comment_form': comment_form})

#@cache_page(60 * 15) # Cache time to live is 15 minutes.
@login_required
def library_new(request):
    if request.method == "POST":
        form = LibraryForm(request.POST, request.FILES)
        if form.is_valid():
            library_file = form.save(commit=False)
            library_file.author = request.user
            library_file.published_date = timezone.now()
            library_file.save()
            return redirect('library_detail', pk=library_file.pk)
    else:
        form = LibraryForm()
    return render(request, 'library_edit.html', {'form': form})

#@cache_page(60 * 15) # Cache time to live is 1 minutes.
@login_required
def library_edit(request, pk):
    post = get_object_or_404(Library, pk=pk)
    if request.method == "POST":
        form = LibraryForm(request.POST, instance=post)
        if form.is_valid():
            library_file = form.save(commit=False)
            library_file.author = request.user
            library_file.published_date = timezone.now()
            library_file.save()
            return redirect('library_detail', pk=library_file.pk)
    else:
        form = LibraryForm(instance=post)
    return render(request, 'library_edit.html', {'form': form})