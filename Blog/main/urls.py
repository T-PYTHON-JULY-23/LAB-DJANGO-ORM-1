from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.home_view, name="home_view"),
    path("main/add_post.html/", views.add_post_view, name="add_post_view"),
    path("main/Posts.html/", views.Posts_view, name="Posts_view")
]