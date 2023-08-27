from django.urls import path,include
from . import views

app_name = 'main'

urlpatterns = [
    path('',views.home_view,name='home_view'),
    path('add/',views.addblog_view,name='addblog_view'),
    path('all/',views.all_bolgs_view,name='all_bolgs_view'),

]