from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post



def add_post_view(request: HttpRequest):

    if request.method == "POST":
        #adding a book
        new_post = Post(title=request.POST["title"], content=request.POST["content"], category=request.POST["category"], publish_date=request.POST["publish_date"])
        new_post.save()
        return redirect("main:all_post_view")

    return render(request, 'main/add_post.html')



def all_post_view(request: HttpRequest):

    posts = Post.objects.all()

    return render(request, "main/all_posts.html", context = {"posts" : posts})


def home_view(request: HttpRequest):
      
    return render(request, "main/home.html")