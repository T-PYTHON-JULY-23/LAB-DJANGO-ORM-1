from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_view, name='blog_view'),
    path('addpost', views.post_view, name='post_view')
]

