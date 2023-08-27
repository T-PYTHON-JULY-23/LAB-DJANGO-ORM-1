from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("add/", views.add_post_view, name="add_post_view"),
    path("all/", views.all_post_view, name="all_post_view")
]
