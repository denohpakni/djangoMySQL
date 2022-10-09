from django.db import models

# Create your models here.
class Contact(models.Model): 
   name = models.CharField(max_length=50) 
   town = models.CharField(max_length=50) 
   county = models.CharField(max_length=10) 
   create_date = models.DateTimeField(auto_now= True) 
   phone_number = models.CharField(max_length=20) 
   email = models.CharField(max_length=20) 

   def __str__(self): 
      return self.name

