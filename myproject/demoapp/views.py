from django.shortcuts import render
from django.http import HttpResponsePermanentRedirect 
from django.urls import reverse 
from .forms import DemoForm 

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

def DemoForm_view(request): 
    form = DemoForm() 
    if request.method == 'POST':
        form = DemoForm(request.POST)
        if form.is_valid():
            try:
                saved_logger = form.save(commit=False)  # ✅ Don't save immediately
                print("Received Data:", request.POST)  # ✅ Print raw form data
                print("Logger Object Before Save:", saved_logger.__dict__)  # ✅ Print field values
                saved_logger.save()  # ✅ Now save to DB
                print("Saved to DB:", saved_logger)  # ✅ Check after saving
            except Exception as e:
                print("❌ Database Error:", e)
        else:
            print("❌ Form Errors:", form.errors)
    context = {'form': form}
    return render(request, 'home.html', context) 