from django import forms
import re

class SignupForm(forms.Form):
    uname = forms.CharField()
    uemail = forms.EmailField()

    def clean_uname(self):
        input_uname = self.cleaned_data['uname']
        if len(input_uname) < 8:
            raise forms.ValidationError("Minimum Length for user name is 8")
        return input_uname

    def clean_uemail(self):
        input_email = self.cleaned_data['uemail']
        valid_gmail_email =  re.match('\w+@gmail.com$',input_email)
        if valid_gmail_email == None:
            raise forms.ValidationError("Only Gmail id are avialble")
        return input_email


class FeedbackForm(forms.Form):
    uname = forms.CharField()
    uemail = forms.EmailField()
    upass = forms.CharField(widget=forms.PasswordInput)

    def clean_uname(self):
        input_uname = self.cleaned_data['uname']
        if len(input_uname) < 8:
            raise forms.ValidationError("Minimum Length for user name is 8")
        return input_uname

    def clean_uemail(self):
        input_email = self.cleaned_data['uemail']
        valid_gmail_email =  re.match('\w+@gmail.com$',input_email)
        if valid_gmail_email == None:
            raise forms.ValidationError("Only Gmail id are avialble")
        return input_email


