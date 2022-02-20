from django.http import HttpResponseRedirect
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


class HomeView(View):

    formclass = PostForm
    mypost = Post.objects.filter().order_by("-date")

    def get(self, request, *args, **kwargs):

        form = self.formclass()
        myuser = request.session.get('customer')
        try:
            myuserdata = Registration.objects.get(pk=myuser)
        except:
            myuserdata = None

        try:
            userprofile = UserProfile.objects.get(user=myuserdata)
        except:
            userprofile = None

        return render(request, 'home.html', {'fm': form,  'myuserdata': myuserdata, 'mypost':  self.mypost, 'myuser': myuserdata, "userprofile": userprofile})

    def post(self, request, *args, **kwargs):
        mypost = Post.objects.filter().order_by("-date")
        form = PostForm(request.POST, request.FILES)
        n = request.session.get('customer')
        myuser = Registration.objects.get(id=n)
        userprofile = UserProfile.objects.get(user=myuser)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = myuser
            obj.myprofile = userprofile
            obj.save()
        return render(request, "home.html", {'fm': self.formclass(), 'mypost':  mypost})


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
