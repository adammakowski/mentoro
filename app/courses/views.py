from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Course
from .forms import CourseForm
# Create your views here.

# @cache_page(60 * 1) # Cache time to live is 1 minutes.
def courses_all(request):
    courses = Course.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'courses_all.html', {'courses': courses})
# @cache_page(60 * 1) # Cache time to live is 1 minutes.
def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'course_detail.html', {'course': course})
# @cache_page(60 * 1) # Cache time to live is 1 minutes.
def course_new(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.author = request.user
            course.published_date = timezone.now()
            course.save()
            return redirect('course_detail', pk=course.pk)
    else:
        form = CourseForm()
    return render(request, 'course_edit.html', {'form': form})
# @cache_page(60 * 1) # Cache time to live is 1 minutes.
def course_edit(request, pk):
    post = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=post)
        if form.is_valid():
            course = form.save(commit=False)
            course.author = request.user
            course.published_date = timezone.now()
            course.save()
            return redirect('course_detail', pk=post.pk)
    else:
        form = CourseForm(instance=post)
    return render(request, 'course_edit.html', {'form': form})