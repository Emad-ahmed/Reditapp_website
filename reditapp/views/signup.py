from django.contrib.auth.hashers import check_password
from email import message
import imp
from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from reditapp.forms import RegistrationForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from reditapp.models.registration import Registration
from reditapp.models.userprofile import UserProfile
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.contrib.auth.models import User


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


class ProfileView(View):
    def get(self, request):
        try:
            myuser = request.session.get('customer')
            n = request.user.is_superuser
            if not n:
                try:
                    myuserdata = Registration.objects.get(pk=myuser)
                except:
                    myuserdata = None
                fm = RegistrationForm(instance=myuserdata)
                profileform = ProfileForm()
                userprofile = UserProfile.objects.get(user=myuserdata)
                return render(request, 'profile.html', {'form': fm, 'profileform': profileform, "userprofile": userprofile})
            else:
                m = request.user.email
                mymail = User.objects.get(email=m)
                return HttpResponse("You Are Admin")
        except:
            myuser = request.session.get('customer')
            myuserdata = Registration.objects.get(pk=myuser)
            fm = RegistrationForm(instance=myuserdata)
            profileform = ProfileForm()
            return render(request, 'profile.html', {'form': fm, 'profileform': profileform})

    def post(self, request):
        myuser = request.session.get('customer')
        myuserdata = Registration.objects.get(pk=myuser)
        if 'updateform' in request.POST:
            name = request.POST.get("name")
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            university = request.POST.get("university")
            departMent = request.POST.get("departMent")

            fm = Registration.objects.filter(id=myuser).update(name=name, email=email, phone=phone,
                                                               university=university, departMent=departMent)
        elif 'profile' in request.POST:
            if len(request.FILES) != 0:
                profile_photo = request.FILES['profile_photo']

            profileform = UserProfile(
                user=myuserdata, profile_photo=profile_photo)
            profileform.save()

        return HttpResponseRedirect(reverse_lazy('profile'))


def change_password(request):
    if request.method == "POST":
        old_password = request.POST.get("oldpassword")
        new_pass = request.POST.get("newpassword")

        print(old_password)

        myuser = request.session.get('customer')
        myuserdata = Registration.objects.get(pk=myuser)
        print(myuserdata.password)
        name = check_password(old_password, myuserdata.password)
        n = make_password(new_pass)
        if name:
            reg = Registration.objects.filter(
                id=myuserdata.id).update(password=n)

        else:
            return HttpResponse("Old Password Not Match")

    return render(request, "change_password.html")
