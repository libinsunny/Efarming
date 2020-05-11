
from django.db import models
from django.conf import settings
from django.contrib.auth.models import auth,User

# Create your models here.
class UserRegister(models.Model):
    userid = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100)
    usertype = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100,default="") 
    housename = models.CharField(max_length=100,default="")
    place = models.CharField(max_length=100,default="")
    city = models.CharField(max_length=100,default="")
    pin = models.CharField(max_length=100,default="")
    district = models.CharField(max_length=100,default="")
    
    
    
    def __str__(self):
        return self.email