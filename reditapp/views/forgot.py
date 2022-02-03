import imp
from django.shortcuts import render


def forgot_password(request):
    return render(request, 'forgot.html')
