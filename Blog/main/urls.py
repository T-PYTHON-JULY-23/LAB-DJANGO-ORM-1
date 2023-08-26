from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.home, name="home_view"),
    path('posts/', views.all_recpies, name="post_view"),
    path('add/', views.addRecpie, name="add_recpie"),
    ]