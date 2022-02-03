from django.urls import path
from reditapp.views import HomeView, SignupView, LoginView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
]
