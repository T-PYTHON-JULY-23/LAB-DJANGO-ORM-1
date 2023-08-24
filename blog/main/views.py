from django.shortcuts import render
from django.http import HttpRequest , HttpResponse 
from . import views
from .models import Post
# Create your views here.


def home_view(request : HttpRequest):

    return render(request,'main/home.html')

def add_view(request:HttpRequest):
    if request.method =='POST':
        new_post=Post(title=request.POST['title'],content=request.POST['content'],publish_date=request.POST['publish_date'],category=request.POST['category'])
        new_post.save()
        
    return render(request , 'main/add.html')

def all_blogs_view(request:HttpRequest):
    posts = Post.objects.all()

    return render(request, "main/all_posts.html", context = {"posts" : posts})
