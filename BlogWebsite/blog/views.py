from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import post


# Create your views here.


def home(request:HttpRequest):
    return render(request,'blog/home.html')

def add_post(request:HttpRequest):
    if request.method == 'POST':
        new_post = post(title=request.POST['title'], content=request.POST['content'], category=request.POST['category'], publish_date=request.POST['publish_date'])
        new_post.save()

        return redirect("blog:all_post_view")

    return render(request,'blog/add_post.html')


def view_post(request:HttpRequest):
    posts = post.objects.all()

    return render(request,'blog/all_post.html', context={'posts':posts} )
