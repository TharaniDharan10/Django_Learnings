from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("This is home of myapp")

# return JSON response
def data(request):
    data = {
        "name": "John",
        "age": 21,
        "city": "New York",
        "course": "INT253"
    }
    return JsonResponse(data)

# return if a number is even or odd
def even_odd(request):
    number = 21
    if number % 2 == 0:
        return HttpResponse(f"{number} is even")
    else:
        return HttpResponse(f"{number} is odd")

# render an HTML file from templates
def htmlfile(request):
    return render(request, 'index.html')

# pass a variable or data into HTML file
def datafile(request):
    a = "Django is a web framework of Python"
    return render(request, 'index.html', {"data": a})

def display(req, username):
    return HttpResponse(f"Username: {username}")

# year view
def year(request, year):
    return HttpResponse(f"Year: {year}")

def uservalue(request, name):
    return HttpResponse(f"Name: {name}")

def website(request, data):
    try:
        data = 10 / data
        return HttpResponse(f"Result: {data}")
    except ZeroDivisionError:
        return HttpResponse("Error: Division by zero is not allowed.")
    except TypeError:
        return HttpResponse("Error: Please provide a valid number.")
