from django.urls import path 
from . import views 

app_name='demoapp'
urlpatterns = [ 
    path('', views.home, name='home'), 
    path('drinks/<str:name>', views.drinks, name="drinks"),
    path('dishes/<str:dish>', views.menuitems),
] 