from django.shortcuts import render,redirect
from sendAmail.forms import LoginForm,EmailForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
import datetime
from django.core.mail import send_mail
from sendAmail.models import EmailModel,UserProfile
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')



def registrationPage(request):

    if request.user.is_authenticated:
        return redirect('dashBoard')

    registrationForm = UserCreationForm()
    if request.method == 'POST':
        registrationForm = UserCreationForm(request.POST)
        if registrationForm.is_valid():
            registeredUserDetails = User()
            registeredUserDetails.username = registrationForm.cleaned_data['username']
            registeredUserDetails.set_password(registrationForm.cleaned_data['password1'])


            registeredUserDetails.save()
            request.session['message'] = 'Registration done successfully!'
            return redirect('login')
    return render(request,'registration_page.html',{'registration_form':registrationForm})




def loginForm(request):

    if request.user.is_authenticated:
        return redirect('dashBoard')

    login_form = LoginForm()
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            userAuthenticate = authenticate(username = username , password = password)
            if userAuthenticate is None:
                return render(request, 'login_page.html',{'login_form': login_form, 'msg': 'User not found'})
            else:
                login(request, userAuthenticate)
                request.session['city'] = 'Bangalore'
                print(request.user.username)
                return redirect('dashBoard')

    if 'message' in request.session:
        msg = request.session['message']
        del request.session['message']
        return render(request, 'login_page.html', {'login_form': login_form,'msg': msg})

    else:
        return render(request,'login_page.html',{'login_form':login_form,'msg':''})


def replyHere(request):

    now = datetime.datetime.now()
    html = '<html><head><body> it is now %s </body></head></html>' %now
    return HttpResponse(html)


@login_required(login_url='/sign_in')
def dashboard(request):
    return render(request,'dashboard.html')

@login_required(login_url='/sign_in')
def sendMail(request):
    mailFormData = EmailForm()
    if request.method == 'POST':
        mailFormData = EmailForm(request.POST)
        if mailFormData.is_valid():
            mailModel = EmailModel()
            mailModel.to_mail = mailFormData.cleaned_data['to_mail']
            mailModel.from_mail = mailFormData.cleaned_data['from_mail']
            mailModel.message = mailFormData.cleaned_data['message']
            mailModel.save()
            sendingMail = send_mail('test_Mail',mailModel.message,mailModel.from_mail, [mailModel.to_mail])
            return HttpResponse(sendingMail)

    return render(request,'send_mail.html',{'mailFormData':mailFormData})


def signOut(request):
    logout(request)
    return redirect('login')
    #registrationForm = LoginForm()
    #return render(request,'registration_page.html',{'registration_form':registrationForm})

# Create your views here.
