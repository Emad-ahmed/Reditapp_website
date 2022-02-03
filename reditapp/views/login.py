import imp
from django.shortcuts import render
from django.views import View
from reditapp.forms import RegistrationForm


class LoginView(View):
    def get(self, request):
        return render(request, 'signup.html')
