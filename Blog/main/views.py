from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Recpie


# Create your views here.
def home(request: HttpRequest):

    return render(request, "main/home.html")


def addRecpie(request: HttpRequest):
     
     if request.method == "POST":
        #adding a recpes
        new_recpie = Recpie(title_recipes=request.POST['title_recipes'],category=request.POST['category'],Ingredients=request.POST['Ingredients'],Instructions=request.POST['Instructions'],publish_date=request.POST['publish_date'])
        new_recpie.save()
        return redirect("main:post_view")

        

     return render(request, "main/addRecipe.html")

def all_recpies(request: HttpRequest):

    recpies = Recpie.objects.all()

    return render(request, "main/post.html", context = {"recpies" : recpies})