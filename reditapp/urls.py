from django.urls import path
from reditapp.views import CSE, HomeView, SignupView, LoginView, forgot_password, logout, CSEView, ShowCSEView, ShowDetailView, ProfileView, ShareFileView, likepost

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('loginview/', LoginView.as_view(), name='loginview'),
    path('signupview/', SignupView.as_view(), name='signupview'),
    path('cse/', CSEView.as_view(), name='cse'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('share/', ShareFileView.as_view(), name='share'),
    path('showdetail/<int:id>/', ShowDetailView.as_view(), name='showdetail'),
    path('showcse/<int:num>/', ShowCSEView.as_view(), name='showcse'),
    path('forgot_password/', forgot_password, name='forgot_password'),
    path('logout', logout, name="logout"),
    path('likepost/<int:id>/', likepost, name="likepost"),

]
