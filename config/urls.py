# config/urls.py

# Django modules
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    # user_interface
    path('', include('apps.user_interface.urls', namespace='user_interface')),

    # Django Rest Framework
    path('api-auth/', include('rest_framework.urls')),

    # Django Admin
    path('admin/', admin.site.urls),
]
