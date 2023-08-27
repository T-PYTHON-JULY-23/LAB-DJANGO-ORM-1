from django.urls import path 
from . import views

app_name ="main"

urlpatterns=[
    path("",views.home_view,name="home_view"),
    path("add_post/",views.add_post,name="add_post"),
    path("all_recipes/",views.all_recipes_view,name="all_recipes_view")

]