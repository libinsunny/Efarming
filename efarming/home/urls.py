from django.urls import path
from .import views


urlpatterns = [

   path('', views.index, name='index'),
   path('login/', views.login, name='login'),
   path('register/', views.register, name='register'),
   path('index/', views.index, name='home'),
   path('homeproduct/', views.homeproducts, name='homeproduct'),
  # path('farmer/farmerhomepage/', views.farmerhomepage, name='farmerhomepage'),
  
]