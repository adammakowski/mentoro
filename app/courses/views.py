from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.cache import cache_page
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Course, Category, Lesson
from .forms import CourseForm, LessonForm
# Create your views here.

#@cache_page(60 * 15) # Cache time to live is 15 minutes.
def courses_all(request):
    courses = Course.objects.filter(status=1).order_by('-created_date')
    categories = Category.objects.all()
    context = {'courses': courses, 'categories': categories}
    return render(request, 'courses_all.html', context)

#@cache_page(60 * 15) # Cache time to live is 15 minutes.
def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    lessons = Lesson.objects.all()
    context = {'lessons': lessons, 'course': course}
    return render(request, 'course_detail.html', context)

#@cache_page(60 * 15) # Cache time to live is 15 minutes.
@login_required
def course_new(request):
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save(commit=False)
            course.author = request.user
            course.published_date = timezone.now()
            course.save()
            return redirect('course_detail', pk=course.pk)
    else:
        form = CourseForm()
    return render(request, 'course_edit.html', {'form': form})


@login_required
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

#@cache_page(60 * 15) # Cache time to live is 1 minutes.
# def lessons_all(request):
#     lessons = Lesson.objects.all()
#     context = {'lessons': lessons}
#     return render(request, 'course_detail.html', context)

@login_required
def course_lesson_new(request):
    if request.method == "POST":
        form = LessonForm(request.POST, request.FILES)
        if form.is_valid():
            course_lesson = form.save(commit=False)
            course_lesson.author = request.user
            course_lesson.published_date = timezone.now()
            course_lesson.save()
            return redirect('course_detail', pk=course_lesson.pk)
    else:
        form = LessonForm()
    return render(request, 'course_lesson_edit.html', {'form': form})

def category_list(request):
    categories = Category.objects.all()  # this will get all categories, you can do some filtering if you need (e.g. excluding categories without posts in it)
    context = {'categories': categories}
    return render(request, 'courses_categories.html', context)  # blog/category_list.html should be the template that categories are listed.


def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    course = Course.objects.filter(status=1).order_by('-created_date')
    course = course.filter(category=category)
    context = {'course': course, 'category': category}
    return render(request, 'course_category_detail.html', context)  # in this template, you will have access to category and posts under that category by (category.post_set).