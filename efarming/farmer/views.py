from django.shortcuts import render
from officer.models import product,application,technique
from django.contrib.auth.models import User, auth

from home.models import UserRegister
from.models import cart
from django.template.loader import render_to_string
import json
from django.db.models import Subquery,OuterRef
#from django.http import HttpResponse

# Create your views here.


def farmerhomepage(request):
    username = request.session['username']

    return render(request, 'farmerhomepage.html', {'username': username})



def products(request):

    allproducts=product.objects.all().order_by('-productid')
    print(allproducts)
    params={'allproducts':allproducts}

    

    return render(request, 'product.html',params)

    #return render_to_string('product.html').render(params, request=request)



def singleproduct(request,productid):

    pro=product.objects.filter(productid=productid)
    return render(request, 'singleproduct.html',{'pro':pro[0]})



def viewcart(request):
    username = request.session['username']
    userprod=cart.objects.filter(user=username).values_list('productid', flat=True)
    print(userprod)
    prod=product.objects.filter(productid__in=userprod)
    #prod=product.objects.filter(productid=Subquery(userprod.values('productid')))
    print(prod)


    total=0
    for item in prod:
        total+=item.price

        


    return render(request, 'cart.html',{'prod':prod,'total':total})



def addtocart(request,productid):

    username = request.session['username']

    #proid=product.objects.filter(productid=productid)
    userid=UserRegister.objects.filter(userid=1)
    #print(proid[0])
    #u=UserRegister.objects.values('userid').filter(email=username)
    #u=UserRegister.objects.only('userid').get(email=username).userid
    quantity=0
    price=0 
    prod=product.objects.filter(productid=productid)
    for item in prod:
        quantity=item.quantity
        price=item.price



    c=cart(productid=productid,user=username,quantity=quantity,total=price)
    c.save()

    username = request.session['username']
    userprod=cart.objects.filter(user=username).values_list('productid', flat=True)
    print(userprod)
    prod=product.objects.filter(productid__in=userprod)
    #prod=product.objects.filter(productid=Subquery(userprod.values('productid')))
    print(prod)

    #clist=[]
    #for item in cartprod:
        #prod=product.objects.filter(productid=item.productid)
        #p.append([prod])
        #clist=clist | prod
        #print(clist)
    total=0
    for item in prod:
        total+=item.price

        


    return render(request, 'cart.html',{'prod':prod,'total':total})





def viewapplication(request):

    allapps=application.objects.all().order_by('-applicationId')
    print(allapps)
    params={'allapps':allapps}
   

    return render(request, 'farmerapplication.html',params)




def viewtechnique(request):

    alltech=technique.objects.all().order_by('-techniqueId')
    
    params={'alltech':alltech}
   

    return render(request, 'farmerviewtechniques.html',params)



def farmerprofile(request):
    username = request.session['username']
    user=User.objects.filter(username=username)

    details=UserRegister.objects.filter(email=username)
    params={'user': user[0], 'details': details[0]}
    print(params)
 
    return render(request, 'farmerprofile.html',params)

      



def deletecart(request,productid):

    username = request.session['username']

    instance = cart.objects.filter(productid=productid,user=username)
    instance.delete()
    
    userprod=cart.objects.filter(user=username).values_list('productid', flat=True)
    print(userprod)
    prod=product.objects.filter(productid__in=userprod)
    #prod=product.objects.filter(productid=Subquery(userprod.values('productid')))
    print(prod)


    total=0
    for item in prod:
        total+=item.price

        


    return render(request, 'cart.html',{'prod':prod,'total':total})

