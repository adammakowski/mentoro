from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Mentor
from .forms import MentorForm
from django.contrib.auth.decorators import login_required

def mentors_all(request):
    mentors = Mentor.objects.filter(active=True, status=1).order_by('-created_date')
    context = {'mentors':mentors}
    return render(request, 'mentors_all.html', context)

def mentors_detail(request, pk):
    mentors = get_object_or_404(Mentor, pk=pk)
    return render(request, 'mentors_detail.html', {'mentors': mentors})

@login_required
def mentors_new(request):
    if request.method == "POST":
        form = MentorForm(request.POST, request.FILES)
        if form.is_valid():
            mentor = form.save(commit=False)
            mentor.author = request.user
            mentor.published_date = timezone.now()
            mentor.save()
            return redirect('mentors_new_success')
    else:
        form = MentorForm()
    return render(request, 'mentors_edit.html', {'form': form})

def mentors_new_success(request):
    return render(request, 'mentors_new_success.html', {})