from django.contrib import admin
from django.urls import path, include
from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('help/', views.help, name='help'),
    path("", include("myapp.urls")),
    path('about2/', views.about2),
    path('dynamicdata/', views.dynamic),
    path("dynamicsum/", views.dynamicsum),
    path('ifelse/', views.ifelse),
    path('ifelsebyurl/<int:age>', views.ifelsebyurl)
]
