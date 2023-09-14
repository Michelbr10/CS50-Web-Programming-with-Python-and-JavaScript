from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#def index(request):
#    return HttpResponse("Hello, world.")

def index(request):
    return render(request, "hello/index.html")

# def hello(request, name):
#     return HttpResponse(f"Hello, {name.capitalize()}!")

def hello(request, name):
    return render(request, "hello/hello.html", {
        'name': name.capitalize()
    })
