from django.shortcuts import HttpResponse

def home(request):
    return HttpResponse("Home Page")
def about(request):
    return HttpResponse("About Page")
def contact(request):
    return HttpResponse("Contact Page")
def help(request):
    return HttpResponse("Help Page")