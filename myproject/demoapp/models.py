from django.db import models
from unicodedata import name

# Create your models here.
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