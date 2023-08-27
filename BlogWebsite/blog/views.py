from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Blog


# Create your views here.


def add_post_view(request: HttpRequest):

    if request.method == "POST":
        #adding a post
        new_post = Blog(title=request.POST["title"], Content=request.POST["Content"], category= request.POST["category"], publish_date=request.POST["publish_date"])
        new_post.save()

        return redirect("blog:all_post_view")

    return render(request, 'blog/add_post.html')



def all_post_view(request: HttpRequest):

    blog = Blog.objects.all()

    return render(request, "blog/all_post.html", context = {"blog" : blog})