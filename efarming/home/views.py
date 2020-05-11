from django.shortcuts import render,redirect,reverse
from.models import UserRegister
import json
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from officer.models import product

# Create your views here.



def index(request):
    return render(request, 'index.html')


def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
                auth.login(request, user)
                if User.objects.filter(last_name="admin", username=username).exists():
                    request.session['username']=username
                    return redirect('adminhomepage')

                   
                else:
                     request.session['username']=username

                     return redirect('farmerhomepage')

                #return render(request, 'farmer/farmerhomepage.html')
                #return render(request, 'home.html')
                #return redirect(reverse('farmerhomepage', kwargs={"username": username}))
               
                
        else:
                messages.info(request, 'invalid credintial')
                return redirect('login')
    else:
        return render(request, 'login.html')

    

def register(request):
    if request.method == 'POST':
        firstName =request.POST['firstname']
        lastName = request.POST['lastname']
        email =request.POST['email']
        password = request.POST['password']
        password1 = request.POST['confirmpassword']
        usertype ="farmer"

        if(password == password1):
             if User.objects.filter(username=email).exists():
                  messages.info(request,'Email already taken')
                  return redirect('register')
            
             else:
                 user = User.objects.create_user(username=email, password=password, email=email, first_name=firstName, last_name=lastName)
                 user.save()

                 u=UserRegister(email=email,usertype=usertype)
                 u.save()
            
                 return redirect('login')

        else:
            messages.info(request,'Password Missmatch')
            return redirect('register')          
              
    else:
        return render(request, 'register.html')    






def homeproducts(request):

    allproducts=product.objects.all().order_by('-productid')
    print(allproducts)
    params={'allproducts':allproducts}

    

    return render(request, 'homeproduct.html',params)




