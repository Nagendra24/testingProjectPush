from django.conf.urls import url
from sendAmail import views

urlpatterns=[
    url(r'^registration$',views.registrationPage,name='SignUp'),
    url(r'sign_in',views.loginForm,name='login'),
    url(r'logout',views.signOut,name='LogOut'),
    url(r'dashboard',views.dashboard,name='dashBoard'),
    url(r'replyHere',views.replyHere,name='replyHere'),
    url(r'send_mail',views.sendMail,name='sendMail'),
]

