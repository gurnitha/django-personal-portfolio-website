# user_interface/urls.py

# Django modules
from django.urls import path

# Locals
from apps.user_interface import views  

app_name = 'user_interface'

urlpatterns = [

    path('', views.index, name='index'),
    
]
