from django.conf.urls import url
from sendAmail import views

urlpatterns=[
    url(r'^registration$',views.registrationPage,name='SignUp'),
    url(r'sign_in',views.loginForm,name='login'),
    url(r'logout',views.signOut,name='LogOut'),
    url(r'dashboard',views.dashboard,name='dashBoard'),
    url(r'replyHere',views.replyHere,name='replyHere'),
    url(r'send_mail',views.sendMail,name='sendMail'),
    #url(r'^$', views.home, name='home'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]

