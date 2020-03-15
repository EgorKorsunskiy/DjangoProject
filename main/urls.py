from django.urls import path
from .views import MainView, MainLoginView

app_name = 'main'
urlpatterns = [
    path('', MainView.as_view(), name='index_main'),
    path('user=<str:user>', MainLoginView.as_view(), name='login_main')
]
