from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Post

def home_view(request: HttpRequest):

    return render(request, "main/home.html")

def add_post_view(request: HttpRequest):
    if request.method == "POST":
        new_post = Post(title=request.POST["title"], content=request.POST["content"], category=request.POST["category"], publish_date=request.POST["publish_date"])
        new_post.save()

        return redirect("main:all_posts_view")

    return render(request, 'main/add_post.html')



def all_posts_view(request: HttpRequest):

    posts = Post.objects.all()

    return render(request, "main/posts.html", context = {"posts" : posts})
    # return render(request, "main/posts.html")