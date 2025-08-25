from os import name
import re
from django.shortcuts import HttpResponse, render

from myapp import views

def home(request):
    return HttpResponse("Home Page")
def about(request):
    return HttpResponse("About Page")
def contact(request):
    return HttpResponse("Contact Page")
def help(request):
    return HttpResponse("Help Page")
def about2(req):
    return render(req, 'about.html')
def dynamic(req):
    name = "Daniel Joseph"
    age = 21
    return render(req, 'dynamic.html',{"name": name, "age": age})

def dynamicsum(req):
    x=10
    y=20
    return render(req, 'dynamic2.html', {"x": x, "y": y, "sum": x+y})

def ifelse(req):
    age = 18
    return render(req, 'ifelse.html', {'age' : age})

def ifelsebyurl(req, age):
    return render(req, 'ifelse.html', {'age' : age})