from django.shortcuts import render
from formsapp.forms import SignupForm,FeedbackForm
from formsapp.models import Signupdata,Feedbackdata
from django.contrib.auth.hashers import make_password

# Create your views here.
def signup(request):
    form = SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            print("Name:",form.cleaned_data['uname'])
            print("Email:",form.cleaned_data['uemail'])
            name = form.cleaned_data['uname']
            email = form.cleaned_data['uemail']
            signup_data = Signupdata(username=name,email_id=email)
            signup_data.save()
    return render(request,'signupform.html',{'form':form})

def feedback(request):
    form = FeedbackForm()
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            print("Name:",form.cleaned_data['uname'])
            print("Email:",form.cleaned_data['uemail'])
            name = form.cleaned_data['uname']
            email = form.cleaned_data['uemail']
            password = make_password(form.cleaned_data['upass'])
            print(password)
            signup_data = Feedbackdata(username=name,email_id=email,password=password)
            signup_data.save()
    return render(request,'feedback.html',{'form':form})


# from django.contrib.auth.hashers import make_password, check_password

# hashed_pwd = make_password("plain_text")
# check_password("plain_text",hashed_pwd)  # returns True
