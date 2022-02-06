import imp
from django.shortcuts import render
from django.views import View
from reditapp.forms import RegistrationForm
from reditapp.models.sharequestion import ShareFile


class CSEView(View):
    def get(self, request):
        return render(request, 'CSE.html')


class ShowCSEView(View):
    def get(self, request, num):
        n = str(num)
        showcse = ShareFile.objects.filter(departMent="CSE", semister=n)

        return render(request, 'ShowCSE.html', {'showcse': showcse})
