from django.db import models
from unicodedata import name
import datetime

# Create your models here.

class Person(models.Model): 
    last_name = models.TextField() 
    first_name = models.TextField() 

    def __str__(self): 
        return f"{self.last_name}, {self.first_name}" 
#Menu Category
#Menu
class MenuCategory(models.Model):
    menu_category_name = models.CharField(max_length=200)
class Menu(models.Model):
    menu_item = models.CharField(max_length = 200, default="Default Item")
    price = models.IntegerField(default=0)
    category_id = models.ForeignKey(MenuCategory, on_delete=models.PROTECT, default=None, related_name="category_name")

    def __str__(self):
        return self.name + ":" + self.cuisine

FAVORITE_DISH = [
    ('italian', 'Italian'),
    ('greek', 'Greek'),
    ('turkish', 'Turkish'),
]

class Logger(models.Model):
    first_name = models.CharField(max_length=200, blank=False, null=False)  
    last_name = models.CharField(max_length=200, blank=False, null=False) 
    email = models.EmailField(max_length=200, blank=False, null=False)  
    reservation_date = models.DateField(default=datetime.date.today, blank=False, null=False) 
    favorite_dish = models.CharField(max_length=50, choices=FAVORITE_DISH, blank=False, null=False) 

    def __str__(self):
            return f"{self.first_name} - {self.email}"
class Reservation(models.Model):
    last_name = models.CharField(max_length = 100, blank = True)
    first_name = models.CharField(max_length = 100, blank = True)
    contact = models.CharField("Phone Number", max_length = 300)
    time = models.TimeField()
    count = models.IntegerField()
    notes = models.CharField(max_length = 300, blank = True)

    def __str__(self):
        return self.first_name + " " + self.last_name + " " + self.contact + " " +  self.time.strftime('%H:%M:%S') + " " + str(self.count)

class Employees(models.Model):
    last_name = models.CharField(max_length = 100)
    first_name = models.CharField(max_length = 100)
    role = models.CharField(max_length = 100)
    shift = models.IntegerField()
    