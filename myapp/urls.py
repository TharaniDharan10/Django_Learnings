from django.urls import path, re_path
from . import views

urlpatterns = [
    path('home/', views.home),

    # returns JSON response
    path('data/', views.data),

    path('even_odd/', views.even_odd),

    path('htmlfile/', views.htmlfile),

    path('datafile/', views.datafile),
 
    # string takes in space also 
    path("user1/<str:username>", views.display),
    path("user2/<int:username>", views.display),
    # slug doesnot have space
    path("user3/<slug:username>", views.display),   

    # regex-based routes for year
    re_path(r'^articles/(?P<year>[0-9]{4})/$', views.year),
    re_path(r'^(?P<year>[0-9]{4})/$', views.year),
    re_path(r'^site/(?P<name>[a-z]{2,5})/$', views.uservalue),

    re_path(r"^site1/(?P<name>\w+)/$", views.uservalue),
    re_path(r"^site2/(?P<name>\d+)/$", views.uservalue),

    path("data/<int:data>", views.website)

]
