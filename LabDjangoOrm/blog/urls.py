from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.blog_view, name="blog_view"),
    path("all/", views.all_blog_view, name="all_blog_view"),
    path("add/", views.add_new_blog, name="add_new_blog"),



]