from . import views 
from django.urls import path

urlpatterns = [
    path('home/', views.home),
    
    #returns json response
    path('data/', views.data),

    path("even_odd/", views.even_odd),

    path("htmlfile/", views.htmlfile),

    path("datafile/", views.datafile)
   
]
