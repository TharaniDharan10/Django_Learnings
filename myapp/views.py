from django.http import JsonResponse
from django.shortcuts import render,HttpResponse


def home(request):
    return HttpResponse("This is home of myapp")

# return json response 
def data(request):
    data = {"name" : "John", "age" : 21, "city": "New York", "course": "INT253"}
    return JsonResponse(data)

# return if a number is even or odd 
def even_odd(request):
    number = 21
    if number % 2 == 0:
        # to return a Variable, use f  
        return HttpResponse(f"{number} is even")
    else:
        return HttpResponse(f"{number} is odd")
    
# to render a html file from templates 
def htmlfile(request):
    # to render a html file 
    return render(request, 'index.html')

# to pass a variable or data into html file 
def datafile(request):
    # to render a html file 
    a = "Django is a web framework of Python"
    return render(request, 'index.html', {"data" : a})