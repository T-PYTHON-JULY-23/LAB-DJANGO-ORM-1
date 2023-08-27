from django.shortcuts import render ,redirect
from django.http import HttpResponse , HttpRequest
from .models import Recipe

# Create your views here.

def home_view(request):

    return render(request , 'main/home.html')

def add_post(request):
    if request.method == "POST":
        #adding a Recipe
        new_Recipe = Recipe(title=request.POST["title"], content=request.POST["content"], catagory=request.POST["catagory"], publish_date=request.POST["publish_date"])
        new_Recipe.save()

        return redirect("main:all_recipes_view")
    return render(request,('main/add_post.html'))

def all_recipes_view(request: HttpRequest):

    recipes = Recipe.objects.all()

    return render(request, "main/all_Recipes.html", context = {"recipes" : recipes})
