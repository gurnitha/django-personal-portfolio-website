# config/urls.py

# Django modules
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    # Django Rest Framework
    path('api-auth/', include('rest_framework.urls')),

    # Django Admin
    path('admin/', admin.site.urls),
]
