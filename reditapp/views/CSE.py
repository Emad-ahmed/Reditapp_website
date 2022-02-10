import imp
from django.shortcuts import render
from django.views import View
from reditapp.forms import RegistrationForm
from reditapp.models.sharequestion import ShareFile


class CSEView(View):
    def get(self, request):
        first_semister = ShareFile.objects.filter(semister="1")
        second_semister = ShareFile.objects.filter(semister="2")
        third_semister = ShareFile.objects.filter(semister="3")
        fourth_semister = ShareFile.objects.filter(semister="4")
        fifth_semister = ShareFile.objects.filter(semister="5")
        six_semister = ShareFile.objects.filter(semister="6")
        seven_semister = ShareFile.objects.filter(semister="7")
        eight_semister = ShareFile.objects.filter(semister="8")
        nine_semister = ShareFile.objects.filter(semister="9")
        ten_semister = ShareFile.objects.filter(semister="10")
        eleven_semister = ShareFile.objects.filter(semister="11")
        twelve_semister = ShareFile.objects.filter(semister="12")
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
        return render(request, 'CSE.html', context)


class ShowCSEView(View):
    def get(self, request, num):
        n = str(num)
        showcse = ShareFile.objects.filter(departMent="CSE", semister=n)

        return render(request, 'ShowCSE.html', {'showcse': showcse, 'myactive': 'active'})
