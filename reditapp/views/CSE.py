import imp
from django.shortcuts import render
from django.views import View
from reditapp.forms import RegistrationForm
from reditapp.models import ShareFile, Registration, UserProfile
from django.contrib.auth.models import User


class CSEView(View):
    def get(self, request):

        first_semister = ShareFile.objects.filter(
            semister="1").filter(isthattrue=True)
        second_semister = ShareFile.objects.filter(
            semister="2").filter(isthattrue=True)
        third_semister = ShareFile.objects.filter(
            semister="3").filter(isthattrue=True)
        fourth_semister = ShareFile.objects.filter(
            semister="4").filter(isthattrue=True)
        fifth_semister = ShareFile.objects.filter(
            semister="5").filter(isthattrue=True)
        six_semister = ShareFile.objects.filter(
            semister="6").filter(isthattrue=True)
        seven_semister = ShareFile.objects.filter(
            semister="7").filter(isthattrue=True)
        eight_semister = ShareFile.objects.filter(
            semister="8").filter(isthattrue=True)
        nine_semister = ShareFile.objects.filter(
            semister="9").filter(isthattrue=True)
        ten_semister = ShareFile.objects.filter(
            semister="10").filter(isthattrue=True)
        eleven_semister = ShareFile.objects.filter(
            semister="11").filter(isthattrue=True)
        twelve_semister = ShareFile.objects.filter(
            semister="12").filter(isthattrue=True)
        context = {
            "one": first_semister,
            "two": second_semister,
            "three": third_semister,
            "four": fourth_semister,
            "five": fifth_semister,
            "six": six_semister,
            "seven": seven_semister,
            "eight": eight_semister,
            "nine": nine_semister,
            "ten": ten_semister,
            "eleven": eleven_semister,
            "tweleve": twelve_semister,
            'myactive': 'active'
        }
        try:
            myuser = request.session.get('customer')
            myuserdata = Registration.objects.get(pk=myuser)
            n = request.user.is_superuser
            if not n:
                userprofile = UserProfile.objects.get(user=myuserdata)
                context = {
                    "one": first_semister,
                    "two": second_semister,
                    "three": third_semister,
                    "four": fourth_semister,
                    "five": fifth_semister,
                    "six": six_semister,
                    "seven": seven_semister,
                    "eight": eight_semister,
                    "nine": nine_semister,
                    "ten": ten_semister,
                    "eleven": eleven_semister,
                    "tweleve": twelve_semister,
                    'myactive': 'active',
                    'userprofile': userprofile
                }
                return render(request, 'CSE.html', context)
            else:
                m = request.user.email
                mymail = User.objects.get(email=m)
                return render(request, 'CSE.html', context)

        except:
            return render(request, 'CSE.html', context)


class ShowCSEView(View):
    def get(self, request, num):
        try:
            n = str(num)
            showcse = ShareFile.objects.filter(departMent="CSE", semister=n)
            myuser = request.session.get('customer')
            myuserdata = Registration.objects.get(pk=myuser)
            n = request.user.is_superuser
            if not n:
                userprofile = UserProfile.objects.get(user=myuserdata)
                return render(request, 'ShowCSE.html', {'showcse': showcse, 'myactive': 'active', 'userprofile': userprofile})
            else:
                m = request.user.email
                mymail = User.objects.get(email=m)
                return render(request, 'ShowCSE.html', {'showcse': showcse, 'myactive': 'active'})
        except:
            return render(request, 'ShowCSE.html', {'showcse': showcse, 'myactive': 'active'})
