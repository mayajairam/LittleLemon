#newapp/urls.py 
from django.urls import path 
from newapp import views 
app_name='newapp' 
urlpatterns = [ 
    path('', views.index, name='index'), 
    path('contact/', views.contact, name='contact'),
] 