from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView
from main.models import User


class LoginTemplateView(TemplateView):
    template_name = 'signin/index.html'

    def post(self, request):
        try:
            login_user = User.user.get(full_name=request.POST['username'], password=request.POST['password']).full_name
        except User.DoesNotExist:
            return render(request, 'signin/index.html', {'error_massage': 'please enter correct username and password'})
        return HttpResponseRedirect(reverse('main:login_main', args=(login_user,)))


class RegistrationTemplateView(TemplateView):
    template_name = 'signin/registration.html'

    def post(self, request):
        for name in User.user.only('full_name'):
            if request.POST['username'] == name.full_name:
                return render(request, 'signin/registration.html', {
                    'error_massage': 'Sorry, but this username already exist'
                })
        if request.POST['password'] != request.POST['conf_password']:
            return render(request, 'signin/registration.html', {
                'error_massage': 'The fields Password and Confirm Password must to be same'
                                                                })
        else:
            User.user.create(
                full_name=request.POST['username'],
                email=request.POST['email'],
                age=request.POST['age'],
                password=request.POST['password']
            )
            return HttpResponseRedirect(reverse('signin:login'))
