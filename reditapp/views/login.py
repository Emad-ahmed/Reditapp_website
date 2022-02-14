import imp
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View
from reditapp.forms import RegistrationForm
from reditapp.models import Registration
from django.contrib.auth.hashers import check_password


class LoginView(View):
    def get(self, request):
        LoginView.return_url = request.GET.get('return_url')
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Registration.get_user_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id

                if LoginView.return_url:
                    return HttpResponseRedirect(LoginView.return_url)
                else:
                    LoginView.return_url = None
                    return redirect('home')
            else:
                error_message = 'Email or Password invalid !!'
        else:
            error_message = 'Email or Password invalid !!'

        print(email, password)
        return render(request, 'login.html', {'error': error_message})


def forgot_password(request):
    return render(request, 'forgot_password.html')




def logout(request):
    request.session.clear()
    return redirect('loginview')
