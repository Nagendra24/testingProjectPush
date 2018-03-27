from django import forms
from sendAmail.models import EmailModel,UserProfile

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20,widget=forms.PasswordInput)

class EmailForm(forms.ModelForm):

    message = forms.CharField(max_length=250, widget=forms.Textarea)
    class Meta():
        model = EmailModel
        fields = ('to_mail', 'from_mail', 'message')

    # def clean(self):
    #     form_data = self.cleaned_data
    #
    #     if 'phone_number' in form_data and form_data['phone_number'].isalpha() == True:
    #         self.errors['phone_number'] = ['please provide a valid phone number ! ']

        # class Meta():
        #     model = RegistrationModel
        #     fields = ('name','email','phone_number')