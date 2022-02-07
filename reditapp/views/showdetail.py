import imp
from django.shortcuts import render
from django.views import View
from reditapp.forms import RegistrationForm
from reditapp.models.sharequestion import ShareFile


class ShowDetailView(View):
    def get(self, request, id):
        mysubject = ShareFile.objects.get(pk=id)
        if(mysubject.departMent == "CSE"):
            return render(request, 'ShowDetail.html', {'mysubject': mysubject, 'myactive': 'active'})

        return render(request, 'ShowDetail.html', {'mysubject': mysubject})
