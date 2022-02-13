from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm

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

def draft_list(request):
    drafts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/draft_list.html', {'drafts':drafts})

def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')