import imp
from django.shortcuts import render
from django.views import View
from reditapp.forms import RegistrationForm
from reditapp.models import UserProfile, Registration
from django.http import HttpResponse
from django.contrib.auth.models import User


class HomeView(View):
    def get(self, request):
        try:
            myuser = request.session.get('customer')
            myuserdata = Registration.objects.get(pk=myuser)
            n = request.user.is_superuser
            if not n:
                userprofile = UserProfile.objects.get(user=myuserdata)
                return render(request, 'home.html', {"userprofile": userprofile})
            else:
                m = request.user.email
                mymail = User.objects.get(email=m)
                return render(request, 'home.html')
        except:
            return render(request, 'home.html')
