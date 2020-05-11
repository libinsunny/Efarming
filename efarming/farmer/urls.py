from django.urls import path
from .import views


urlpatterns = [
    path('farmerhomepage/', views.farmerhomepage, name='farmerhomepage'),
    path('product/', views.products, name='product'),
    path('singleproduct/<int:productid>', views.singleproduct, name='singleproduct'),
    path('viewcart/', views.viewcart, name='viewcart'),
    path('addtocart/<int:productid>', views.addtocart, name='addtocart'),
    path('viewapplication/', views.viewapplication, name='viewapplication'),
    path('viewtechnique/', views.viewtechnique, name='viewtechnique'),
    path('farmerprofile/', views.farmerprofile, name='farmerprofile'),
    path('deletecart/<int:productid>', views.deletecart, name='deletecart'),







]