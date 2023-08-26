from django.urls import path
from blog import views

app_name = "blog"

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.posts, name='posts'),
    path('add_post/', views.add_post, name='add_post'),
]