import os
from django.http import FileResponse
from tkinter.messagebox import NO
from django.http import HttpResponseRedirect
from django.http import FileResponse, Http404
from django.http import HttpResponse, HttpResponseNotFound
import imp
from django.shortcuts import get_object_or_404
from turtle import pos
from django.shortcuts import redirect, render
from django.template import Origin
from django.urls import reverse_lazy
from django.views import View
from reditapp.forms import RegistrationForm, PostForm
from reditapp.models import UserProfile, Registration, Post
from django.http import HttpResponse
from django.contrib.auth.models import User
from reditapp.models import Post
from django.views.generic import DetailView
from django.core.files.storage import FileSystemStorage


class HomeView(View):

    def get(self, request, *args, **kwargs):
        myuser = request.session.get('customer')
        if myuser:
            form = PostForm()
            mypost = Post.objects.all().order_by("-id")
            try:
                myuserdata = Registration.objects.get(pk=myuser)
            except:
                myuserdata = None

            try:
                userprofile = UserProfile.objects.get(user=myuserdata)
            except:
                userprofile = None
            return render(request, 'home.html', {'fm': form,  'myuserdata': myuserdata, 'mypost':  mypost, 'myuser': myuserdata, "userprofile": userprofile})
        else:
            return redirect("loginview")

    def post(self, request, *args, **kwargs):
        mypost = Post.objects.all().order_by("-id")
        form = PostForm(request.POST, request.FILES)
        n = request.session.get('customer')
        myuser = Registration.objects.get(id=n)
        try:
            userprofile = UserProfile.objects.get(user=myuser)
        except:
            userprofile = None
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = myuser
            if userprofile:
                obj.myprofile = userprofile
            obj.save()
        return render(request, "home.html", {'fm': form, 'mypost':  mypost})


def likepost(request, id):
    myuser = request.session.get('customer')
    myuserdata = Registration.objects.get(pk=myuser)
    if request.method == "POST":
        post = Post.objects.get(id=id)
        if post.likes.filter(id=myuserdata.id).exists():
            post.likes.remove(myuserdata)
        else:
            post.likes.add(myuserdata)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class ChangePasswordView(View):
    def get(self, request):
        return render(request, "change_password.html")


def show_pdf(request, id):
    myfile = Post.objects.get(id=id)
    pdffile = myfile.postfile

    fs = FileSystemStorage()
    filename = str(pdffile)

    if fs.exists(filename):
        with fs.open(filename) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            # user will be prompted display the PDF in the browser
            response['Content-Disposition'] = 'inline; filename="filename"'

            return response
    else:
        return HttpResponseNotFound('The requested pdf was not found in our server.')
