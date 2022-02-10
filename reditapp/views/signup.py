from email import message
import imp
from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from reditapp.forms import RegistrationForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from reditapp.models.registration import Registration
from reditapp.models.userprofile import UserProfile
from django.urls import reverse_lazy
from django.views.generic import UpdateView


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
        myuser = request.session.get('customer')
        myuserdata = Registration.objects.get(pk=myuser)
        fm = RegistrationForm(instance=myuserdata)
        profileform = ProfileForm()

        try:
            userprofile = UserProfile.objects.get(user=myuserdata)

            return render(request, 'profile.html', {'form': fm, 'profileform': profileform, "userprofile": userprofile})
        except:
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
            password = request.POST.get("name")

            fm = Registration.objects.filter(id=myuser).update(name=name, email=email, phone=phone,
                                                               university=university, departMent=departMent, password=password)
        elif 'profile' in request.POST:
            if len(request.FILES) != 0:
                profile_photo = request.FILES['profile_photo']

            profileform = UserProfile(
                user=myuserdata, profile_photo=profile_photo)
            profileform.save()

        return HttpResponseRedirect(reverse_lazy('profile'))
