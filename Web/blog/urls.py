from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('',views.home_view , name = 'home_view'),
    path('add/', views.add_post_view , name ="add_post_view"),
    path('all/',views.all_posts_view, name="all_posts_view"),
]