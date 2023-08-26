from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('',views.home, name='home_view'),
    path('add_post/',views.add_post,name='add_post_view'),
    path('all_post/',views.view_post,name='all_post_view')
]