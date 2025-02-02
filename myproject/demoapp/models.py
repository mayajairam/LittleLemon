from django.db import models
from unicodedata import name

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length = 100)
    cuisine = models.CharField(max_length = 100)
    place = models.IntegerField

    def __str__(self):
        return self.name + ":" + self.cuisine