from django.shortcuts import render
from.models import product,application,technique



# Create your views here.

def adminhomepage(request):
    username=request.session['username']

    return render(request, 'adminhomepage.html', {'username': username})



def addseed(request):

    if request.method == 'POST':
        
        productName = request.POST['productName']
        #commonName = request.POST['commonName']
        price=request.POST['price']
        quantity=request.POST['quantity']
        productType="seed"
        #image=request.FILE['img']
        desc=request.POST['description']
        image='product/images/' + request.POST['img']
        

        prod=product(productName=productName,price=price,quantity=quantity,productType=productType,description=desc,image=image)
        prod.save()



    return render(request, 'addseed.html')    



def addplant(request):

    if request.method == 'POST':
        
        productName = request.POST['productName']
        #commonName = request.POST['commonName']
        price=request.POST['price']
        quantity=request.POST['quantity']
        productType="plant"
        #image=request.FILE['img']
        desc=request.POST['description']
        image='product/images/' + request.POST['img']
        

        prod=product(productName=productName,price=price,quantity=quantity,productType=productType,description=desc,image=image)
        prod.save()


    return render(request, 'addplant.html')




def products(request):

    allproducts=product.objects.all().order_by('-productid')
    print(allproducts)
    params={'allproducts':allproducts}
    
    return render(request, 'adminproductview.html',params)



def seed(request):

    allproducts=product.objects.filter(productType='seed').order_by('-productid')
    print(allproducts)
    params={'allproducts':allproducts}
    
    return render(request, 'adminproductview.html',params)    



def plant(request):

    allproducts=product.objects.filter(productType='plant').order_by('-productid')
    print(allproducts)
    params={'allproducts':allproducts}
    
    return render(request, 'adminproductview.html',params)  







def deleteProduct(request,productid):


    instance = product.objects.get(productid=productid)
    instance.delete()

    allproducts=product.objects.all().order_by('-productid')
    print(allproducts)
    params={'allproducts':allproducts}
    
    return render(request, 'adminproductview.html',params)




def update(request,productid):
    pro=product.objects.filter(productid=productid)
    print(pro)
    return render(request, 'updateproduct.html',{'pro':pro[0]})


 



def updateProduct(request,productid):



    if request.method == 'POST':
        
        productName = request.POST['productName']
        #commonName = request.POST['commonName']
        price=request.POST['price']
        quantity=request.POST['quantity']
        #productType="plant"
        #image=request.FILE['img']
        desc=request.POST['description']
        image='product/images/' + request.POST['img']

        product.objects.filter(productid=productid).update(productName=productName,price=price,quantity=quantity,description=desc,image=image)
        



   

    allproducts=product.objects.all().order_by('-productid')
    print(allproducts)
    params={'allproducts':allproducts}
    
    return render(request, 'adminproductview.html',params)    





def adapplication(request):
   

    return render(request, 'addapplication.html')




def addapplication(request):

    if request.method == 'POST':
        
        applicationName = request.POST['name']
        requirement1 = request.POST['requirement1']
        requirement2 = request.POST['requirement2']
        requirement3 = request.POST['requirement3']
        requirement4 = request.POST['requirement4']

        notice='application/documents/' + request.POST['notice']
        form='application/documents/' + request.POST['form']
        
        app=application(applicationName=applicationName,requirement1=requirement1,requirement2=requirement2,requirement3=requirement3,requirement4=requirement4,applicationNotice=notice,applicationForm=form) 
        app.save()
       


    return render(request, 'addapplication.html')





def viewapplication(request):

    allapps=application.objects.all().order_by('-applicationId')
    print(allapps)
    params={'allapps':allapps}
   

    return render(request, 'adminviewapplication.html',params)




def deleteApplication(request,applicationId):


    instance = application.objects.get(applicationId=applicationId)
    instance.delete()

    allapps=application.objects.all().order_by('-applicationId')
    print(allapps)
    params={'allapps':allapps}
   

    return render(request, 'adminviewapplication.html',params)



def adtechniques(request):

    return render(request, 'addtechniques.html')


def addtechniques(request):



    if request.method == 'POST':
        
        techName = request.POST['name']
        desc=request.POST['description']
        video='techniques/videos/' + request.POST['video']
        

        tech=technique(techniqueName=techName,description=desc,video=video)
        tech.save()



    return render(request, 'addtechniques.html')  




def viewtechnique(request):

    alltech=technique.objects.all().order_by('-techniqueId')
    
    params={'alltech':alltech}
   

    return render(request, 'adminviewtechniques.html',params)





def deleteTechniques(request,techniqueId):


    instance = technique.objects.get(techniqueId=techniqueId)
    instance.delete()
    
    alltech=technique.objects.all().order_by('-techniqueId')
    
    params={'alltech':alltech}
   

    return render(request, 'adminviewtechniques.html',params)




