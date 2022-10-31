from unittest.util import _MAX_LENGTH
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class book(models.Model):
     id = models.AutoField(auto_created = True, primary_key = True )
     title = models.CharField(max_length = 50)
     author = models.CharField(max_length = 100)
     rating = models.IntegerField(validators = [MaxValueValidator(5), MinValueValidator(1)])
     is_bestselling = models.BooleanField(default = False)
     author_nationality = models.CharField(max_length = 50, null = True)
     

     def __str__(self):
         return f"{self.title} {self.author} ({self.rating})"