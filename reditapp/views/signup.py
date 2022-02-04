from email import message
import imp
from django.shortcuts import render
from django.views import View
from reditapp.forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password


class SignupView(View):
    def get(self, request):
        fm = RegistrationForm()
        return render(request, 'signup.html', {'form': fm})

    def post(self, request):
        fm = RegistrationForm(request.POST)
        if fm.is_valid():
            password = fm.cleaned_data['password']
            mypassword = make_password(password)
            obj = fm.save(commit=False)
            obj.password = mypassword
            obj.save()

            messages.success(request, "Message sent.")
        else:
            messages.error(request, 'Something Wrong')
        return render(request, 'signup.html', {'form': fm})
