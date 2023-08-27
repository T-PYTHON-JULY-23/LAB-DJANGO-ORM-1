from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpRequest
from .models import Blog
# Create your views here.

def home_view(request:HttpRequest):

    return render(request, 'main/home.html')


def addblog_view(request:HttpRequest):
    if request.method == "POST":
       
        new_blog = Blog(title=request.POST["title"], content=request.POST["content"], category=request.POST["category"], publish_date=request.POST["publish_date"])
        new_blog.save()

        return redirect("main:all_bolgs_view")
    return render(request, 'main/add_blog.html')

def all_bolgs_view(request: HttpRequest):

    blogs = Blog.objects.all()

    return render(request, "main/all_blogs.html", context = {"blogs" : blogs})

