from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse
from .models import Blog
# Create your views here.

def blog_view(request:HttpRequest):
    return render(request, 'base.html')

def all_blog_view(request:HttpRequest):
    blogs = Blog.objects.all()

    return render(request,'Posts.html',context = {"blogs":blogs})

def add_new_blog(request:HttpRequest):
    if request.method == "POST":
        new_blog = Blog(title=request.POST["title"],content=request.POST["content"],category=request.POST["category"],publish_date=request.POST["publish_date"])
        new_blog.save()
        return redirect("blog:all_blog_view")
    return render(request, 'Adding.html')
