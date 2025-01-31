from django.shortcuts import render
from django.http import HttpResponsePermanentRedirect 
from django.urls import reverse 

# Create your views here.
from django.http import HttpResponse 
def home(request): 
    return HttpResponse("Hello, world. This is the index view of Demoapp.") 
def about(request):
    return HttpResponse("About us")
def menu(request):
    return HttpResponse("Menu")
def book(request):
    return HttpResponse("Make a booking")
def drinks(request, name):
    query = name
    return HttpResponse("<h1> %s <h1>" %query)
def menuitems(request, dish):
    items = {
        'Alfredopasta':"creamy alredo pasta with chicken",
        'falafel':"delicate falafel with mediterranean sides",
        'Strawberrycheesecake': "soft cheescake with strawberry filling",
    }
    description = items[dish]
    return HttpResponse(f"<h1> {dish} <h1>" + description)