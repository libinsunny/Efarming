from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views




urlpatterns = [
    path('adminhomepage/', views.adminhomepage, name='adminhomepage'),
    path('addseed/', views.addseed, name='addseed'),
    path('addplant/', views.addplant, name='addplant'),
    path('product/', views.products, name='product'),
    path('seed/', views.seed, name='seed'),
    path('plant/', views.plant, name='plant'),
    path('deleteProduct/<int:productid>', views.deleteProduct, name='deleteProduct'),
    path('update/<int:productid>', views.update, name='update'),
    path('updateProduct/<int:productid>', views.updateProduct, name='updateProduct'),
    path('application/', views.addapplication, name='application'),
    path('addapplication/', views.addapplication, name='addapplication'),
    path('viewapplication/', views.viewapplication, name='viewapplication'),
    path('deleteApplication/<int:applicationId>', views.deleteApplication, name='deleteApplication'),
    path('adtechniques/', views.adtechniques, name='adtechniques'),
    path('addtechniques/', views.addtechniques, name='addtechniques'),
    path('viewtechnique/', views.viewtechnique, name='viewtechnique'),
    path('deleteTechniques/<int:techniqueId>', views.deleteTechniques, name='deleteTechniques'),




    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 
         