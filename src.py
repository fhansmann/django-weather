#Edit urls.py file in weather :

from django.contrib import admin 
from django.urls import path, include 
  
  
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('', include('main.urls')), 
] 

#Edit urls.py file in main
from django.urls import path 
from . import views 
  
urlpatterns = [ 
         path('', views.index), 
] 
