import imp
from django.shortcuts import render
from django.views import View
from reditapp.forms import RegistrationForm


class SignupView(View):
    def get(self, request):
        fm = RegistrationForm()
        return render(request, 'signup.html', {'form': fm})

    def post(self, request):
        fm = RegistrationForm(request.POST)
        if fm.is_valid():
            fm.save()
        return render(request, 'signup.html', {'form': fm})
