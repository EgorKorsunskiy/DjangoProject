from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('main.urls', namespace='main')),
    path('login', include('signin.urls')),
    path('ad<int:pk>', include('ad.urls')),
    path('admin/', admin.site.urls)
]
