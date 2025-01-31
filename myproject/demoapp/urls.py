from django.urls import path 
from demoapp import views 

app_name='demoapp'
urlpatterns = [ 
    path('', views.home, name='home'),
    path('about/', views.about, name="about"), 
    path('menu', views.menu, name="menu"), 
    path('book/', views.book, name="book"), 
    path('drinks/<str:name>', views.drinks, name="drinks"),
    path('dishes/<str:dish>', views.menuitems),
] 