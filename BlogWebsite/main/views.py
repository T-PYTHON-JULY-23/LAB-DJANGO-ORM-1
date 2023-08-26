from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse
from .models import BlogWebsite

# Create your views here.

def home_view(request:HttpRequest):

    blogs= BlogWebsite.objects.all()

    return render(request,"main/home_view.html", context = {"blogs" : blogs})

def add_blog_view(request: HttpRequest):

    if request.method == "POST":
        #adding a blog
        new_blog = BlogWebsite(title=request.POST["title"], content=request.POST["content"], category=request.POST["category"],  publish_date=request.POST["publish_date"])
        new_blog.save()

        return redirect("main:home_view")

    return render(request, "main/add_blog_view.html")

