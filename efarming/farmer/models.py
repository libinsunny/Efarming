from django.db import models
from django.conf import settings


# Create your models here.



class cart(models.Model):
    cartid = models.AutoField(primary_key=True)
    user = models.CharField(max_length=100,default="")

    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    productid=models.IntegerField()
    quantity=models.IntegerField()
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)


   
    
    
    
   # def __str__(self):
        #return self.productName

