from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . models import post, comment
from .forms import NewComment
# Create your views here.

def home(request):
    context = {
        'title': 'الصفحه الرئيسيه',
        'posts': post.objects.all(),
    }
    return render(request, 'blog/index.html', context)

def about(request):
    
    return render(request,'blog/about.html', {'title': 'من انا'}, )


def post_detail(request,post_id):
    Post = get_object_or_404(post, pk = post_id)
    Comments = Post.comments.filter(active = True)
    # check before save data from comment form
    if request.method == 'POST':
        comment_form = NewComment(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = Post
            new_comment.save()
            comment_form = NewComment()
    else:
        comment_form = NewComment()
    
  
    context = {
        'title': Post,
        'post': Post,
        'Comments': Comments,
        'comment_form': comment_form,
        }
    
    return render(request,'blog/post_detail.html',context)


