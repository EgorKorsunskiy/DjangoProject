from django.urls import path
from .views import AdView

urlpatterns = [
    path('', AdView.as_view(), name='index')
]
