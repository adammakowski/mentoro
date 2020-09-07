from django.views import generic
from .models import Post
from django.views.generic import ListView
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.cache import cache_page

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_date')
    template_name = 'blog_all.html'
    paginate_by = 3

class PostCreate(generic.CreateView):
    model = Post
    queryset = Post.objects.all()
    template_name = 'blog_new.html'


#@cache_page(60 * 5) # cache 60s * 5 = 5 minutes
def post_detail(request, slug):
    template_name = 'blog_detail.html'
    post = get_object_or_404(Post, slug=slug)
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

    return render(request, template_name, {'post': post, 'comments': comments, 'new_comment': new_comment, 'comment_form': comment_form})

def blog_comment_success(request):
    return render(request, 'blog_comment_success.html', {})