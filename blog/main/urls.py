from django.urls import path,include
from . import views

app_name = 'main'

urlpatterns = [
    path('',views.home_view,name='home_view'),
    path('add/',views.add_view,name='add_view'),
    path('all/',views.all_blogs_view,name='all_blogs_view')
]