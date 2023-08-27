from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.home_page_view, name="home_page_view"),
   path('add/', views.add_new_view, name="add_new_view"),
   path('all/', views.all_new_view, name="all_new_view"),

]