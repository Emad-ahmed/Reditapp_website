from django.urls import path
from reditapp.views import CSE, HomeView, SignupView, LoginView, forgot_password, logout, CSEView, ShowCSEView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('loginview/', LoginView.as_view(), name='loginview'),
    path('signupview/', SignupView.as_view(), name='signupview'),
    path('cse/', CSEView.as_view(), name='cse'),
    path('showcse/<int:num>', ShowCSEView.as_view(), name='showcse'),
    path('forgot_password/', forgot_password, name='forgot_password'),
    path('logout', logout, name="logout")
]
