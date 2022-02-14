import imp
from django.shortcuts import render
from django.views import View
from reditapp.forms import ShareFileForm
from reditapp.models.sharequestion import ShareFile
from django.contrib import messages
from django.conf import Settings, settings
from django.core.mail import send_mail
from reditapp.models import Registration


class ShareFileView(View):
    def get(self, request):
        myshare = ShareFileForm()
        return render(request, 'sharefile.html', {'share': myshare})

    def post(self, request):
        myshare = ShareFileForm(request.POST, request.FILES)
        if myshare.is_valid():
            myshare.save()
            print(myshare)
            myid = myshare.instance.id
            messages.success(request, "Need For Approval Wait!")
            n = request.session.get("customer")
            m = Registration.objects.get(id=n)
            subject = 'welcome to GFG world'

            message = f'Hi {m.name}, Need For Approval \n http://127.0.0.1:8000/admin/reditapp/sharefile/{myid}/change/'
            email_from = m.email
            recipient_list = ["emadahmednew123456789@gmail.com", ]
            send_mail(subject, message, email_from, recipient_list)

        return render(request, 'sharefile.html', {'share': myshare})
