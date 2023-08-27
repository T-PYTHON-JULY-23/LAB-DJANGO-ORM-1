from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
# Create your views here.
from .models import Post

def home_view(request:HttpRequest):
    return render(request, 'main/home.html')

def posts_view(request:HttpRequest):
    posts = Post.objects.all()
    return render(request, 'main/posts.html', {'posts': posts})

def add_post_view(request:HttpRequest):
     if request.method == 'POST':
        new_book = Post(title=request.POST["title"], content=request.POST["content"], category=request.POST["category"], publish_date=request.POST["publish_date"])
        new_book.save()
        return redirect('main:posts_viwe')
     return render(request, 'main/add_post.html')
