from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('posts/', views.posts_view, name='posts_view'),
    path('add_post/', views.add_post_view, name='add_post_view'),
]
