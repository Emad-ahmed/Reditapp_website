from django.urls import path
from reditapp.views import CSE, HomeView, SignupView, LoginView, forgot_password, logout, CSEView, ShowCSEView, ShowDetailView, ProfileView, ShareFileView, likepost, ChangePasswordView, change_password, show_pdf

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('loginview/', LoginView.as_view(), name='loginview'),
    path('signupview/', SignupView.as_view(), name='signupview'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
    path('cse/', CSEView.as_view(), name='cse'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('share/', ShareFileView.as_view(), name='share'),
    path('showdetail/<int:id>/', ShowDetailView.as_view(), name='showdetail'),
    path('showcse/<int:num>/', ShowCSEView.as_view(), name='showcse'),
    path('forgot_password/', forgot_password, name='forgot_password'),
    path('logout', logout, name="logout"),
    path('change_password', change_password, name="change_password"),
    path('likepost/<int:id>/', likepost, name="likepost"),
    path('likepost/<int:id>/', likepost, name="likepost"),
    path('show_pdf/<int:id>/', show_pdf, name="show_pdf"),

]
