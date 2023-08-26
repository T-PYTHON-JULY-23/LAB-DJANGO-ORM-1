from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import post

# Create your views here.

def home_view(request : HttpRequest):

    #to read a cookie
    #mode = request.COOKIES.get("mode", "light")

    return render(request, "main/index.html")


def about_view(request: HttpRequest):

    return render(request, "main/about.html")



def dark_view(request:HttpRequest):

    #setting a cookie   
    response = redirect("main:home_view")
    response.set_cookie("mode", "dark")

    return response


def light_view(request:HttpRequest):
    
    #setting a cookie
    response = redirect("main:home_view")
    response.set_cookie("mode", "light")

    return response
def add_post(request: HttpRequest):

    if request.method == "POST":
        #adding a post
        new_post = post(title=request.POST["title"], description=request.POST["description"], rating= request.POST["rating"], publish_date=request.POST["publish_date"])
        new_post.save()

        return redirect("posts:all_posts")

    return render(request, 'main/add_post.html')


def all_posts(request: HttpRequest):

    posts = post.objects.all()

    return render(request, "main/all_posts.html", context = {"posts" : posts})