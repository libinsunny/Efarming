
# forms.py 
from django import forms 
from .models import product
  
class productForm(forms.ModelForm): 
  
    class Meta: 
        model = product 
        fields = ['productName','commonName','price','quantity','productType','image']



class prodForm(forms.Form):
    
    productName = forms.CharField(max_length=100)
    commonName = forms.CharField(max_length=100)
    price=forms.IntegerField()
    quantity=forms.IntegerField()
    productType=forms.CharField(max_length=100)
    image =forms.ImageField()
    #name = forms.CharField(max_length = 100)
   #picture = forms.ImageFields()
