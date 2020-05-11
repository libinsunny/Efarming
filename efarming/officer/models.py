from django.db import models

# Create your models here.



class product(models.Model):
    productid = models.AutoField(primary_key=True)
    productName = models.CharField(max_length=100)
    
    price=models.IntegerField()
    quantity=models.IntegerField()
    productType=models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    description=models.CharField(max_length=5000,default="")
    image = models.ImageField(upload_to="product/images", default="")
  

    
    def __str__(self):
        return self.productName


class application(models.Model):
    applicationId=models.AutoField(primary_key=True)
    applicationName=models.CharField(max_length=200)
    date=models.DateField(auto_now=True)
    requirement1=models.CharField(max_length=100,default="")
    requirement2=models.CharField(max_length=100,default="")
    requirement3=models.CharField(max_length=100,default="")
    requirement4=models.CharField(max_length=100,default="")
    applicationNotice = models.FileField(upload_to="application/documents", default="")
    applicationForm = models.FileField(upload_to="application/documents", default="")


    def __str__(self):
        return self.applicationName


class technique(models.Model):
    techniqueId=models.AutoField(primary_key=True)
    techniqueName=models.CharField(max_length=200)
    description=models.CharField(max_length=5000,default="")
    date=models.DateField(auto_now=True)
    video = models.FileField(upload_to="techniques/videos", default="")
    

    def __str__(self):
        return self.techniqueName        



