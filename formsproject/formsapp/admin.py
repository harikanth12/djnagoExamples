from django.contrib import admin
from formsapp.models import Signupdata,Feedbackdata
# Register your models here.

class SignupdataAdmin(admin.ModelAdmin):
    list_display = ['id','username','email_id']

admin.site.register(Signupdata,SignupdataAdmin)

class FeedbackdataAdmin(admin.ModelAdmin):
    list_display = ['id','username','email_id']

admin.site.register(Feedbackdata,FeedbackdataAdmin)