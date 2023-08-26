from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.http import HttpRequest, HttpResponse

def home(request: HttpRequest):
    return render(request, 'blog/home.html')

def posts(request: HttpRequest):
    posts = Post.objects.all()
    return render(request, 'blog/posts.html', {'posts': posts})

def add_post(request:HttpRequest):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts')  # Redirect to the posts page after successful submission
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form})

