from django.shortcuts import render
from django.http import HttpResponsePermanentRedirect 
from django.urls import reverse 

# Create your views here.
# Create your views here.
from django.http import HttpResponse 
def index(request): 
    return HttpResponse("Hello, world. This is the index view of Demoapp.") 
def contact(request): 
    return HttpResponse("Hello contact us.") 