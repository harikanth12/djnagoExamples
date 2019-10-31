from django.db import models

# Create your models here.
class Signupdata(models.Model):
    username = models.CharField(max_length=60)
    email_id = models.EmailField()

    def __str__(self):
        return f"Username.-- {self.username}"

class Feedbackdata(models.Model):
    username = models.CharField(max_length=60)
    email_id = models.EmailField()
    password = models.CharField(max_length=60,null=True,blank=True)

    def __str__(self):
        return f"Username.-- {self.username}"

    