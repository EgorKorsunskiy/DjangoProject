from django.urls import path
from .views import LoginTemplateView, RegistrationTemplateView

app_name = 'signin'
urlpatterns = [
    path('', LoginTemplateView.as_view(), name='login'),
    path('/registration', RegistrationTemplateView.as_view(), name='registration')
]