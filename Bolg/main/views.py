from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import NewBlog
# Create your views here.

def add_new_view(request: HttpRequest):

    if request.method == "POST":
        #adding a book
        new_book = NewBlog(title=request.POST["title"], content=request.POST["content"], category=request.POST["category"], publish_date=request.POST["publish_date"])
        new_book.save()

        return redirect("main:all_new_view")


    return render(request, 'main/add_new.html')


def all_new_view(request: HttpRequest):

    new = NewBlog.objects.all()

    return render(request, "main/all_new.html", context = {"new" : new})

def home_page_view(request: HttpRequest):


    return render(request, "main/homePage.html")