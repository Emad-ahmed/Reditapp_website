from django.urls import path
from reditapp.views import HomeView, SignupView, LoginView, forgot_password, logout

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('loginview/', LoginView.as_view(), name='loginview'),
    path('signupview/', SignupView.as_view(), name='signupview'),
    path('forgot_password/', forgot_password, name='forgot_password'),
    path('logout', logout, name="logout")
]
