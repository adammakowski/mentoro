from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.cache import cache_page
from django.utils import timezone
from .models import LibraryFile
from .forms import LibraryForm
# Create your views here.

# cache_page(60 * 1) # Cache time to live is 15 minutes.
def library_all(request):
    library_file = LibraryFile.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'library_all.html', {'library_file': library_file})

# @cache_page(60 * 15) # Cache time to live is 15 minutes.
def library_detail(request, pk):
    library_file = get_object_or_404(LibraryFile, pk=pk)
    return render(request, 'library_detail.html', {'library_file': library_file})

#@cache_page(60 * 15) # Cache time to live is 15 minutes.
def library_new(request):
    if request.method == "POST":
        form = LibraryForm(request.POST)
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
def library_edit(request, pk):
    post = get_object_or_404(LibraryFile, pk=pk)
    if request.method == "POST":
        form = LibraryForm(request.POST, instance=post)
        if form.is_valid():
            library_file = form.save(commit=False)
            library_file.author = request.user
            library_file.published_date = timezone.now()
            library_file.save()
            return redirect('library_detail', pk=post.pk)
    else:
        form = LibraryForm(instance=post)
    return render(request, 'library_edit.html', {'form': form})