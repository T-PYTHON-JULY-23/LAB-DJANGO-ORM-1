from django.urls import path
from blog.views import home, posts, add_post, delete_post

urlpatterns = [
    path('', home, name='home'),
    path('posts/', posts, name='posts'),
    path('add-post/', add_post, name='add_post'),
    path('delete_post/<int:post_id>/', delete_post, name='delete_post'),
]
