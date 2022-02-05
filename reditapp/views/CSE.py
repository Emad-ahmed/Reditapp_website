import imp
from django.shortcuts import render
from django.views import View
from reditapp.forms import RegistrationForm


class CSEView(View):
    def get(self, request):

        return render(request, 'CSE.html')
