from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Comment, Post
from django.utils import timezone
from .forms import PostForm, CommentForm

# Create your views here.
# connects template abd models
def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
    # ↓ the code shows super ugly error, if there is no post with the given pk does not exist
    # post = Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

@login_required
def post_new(request):
    if request.method == 'POST':
        # we have more data in request.POST
        form = PostForm(request.POST)
        
        if form.is_valid():
            # 'commit=False' : we do not save Post model yet (before doing that, we have to save author name)
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            
            # 'post_detail' is the name of the view we want to go to
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form':form})

# give pk values from urls.py
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    # after an user saved the post
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            
            return redirect('post_detail', pk=post.pk)
        
    else:
        form = PostForm(instance=post)
    
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def draft_list(request):
    drafts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/draft_list.html', {'drafts':drafts})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        # we have more data in request.POST
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form':form})

def comment_list(request):
    comments = Comment.objects.filter(approved_comment = False).all()
    
    return render(request, 'blog/comment_list.html', {'comments': comments})

def approve_comment(request, pk):
    print("clicked")
    
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    print("post_detail")
    
    return redirect('post_detail', pk=comment.post.pk)
    
    