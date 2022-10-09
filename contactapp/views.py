from django.shortcuts import render
from django.http import HttpRequest
from .models import Contact
import datetime

# Create your views here.

def homepage(request):
    return render(request, 'base.html')

def contact(request): 
   """Renders the contact page."""
   assert isinstance(request, HttpRequest) 

   # Retrieve all contacts in the database table
   contact_list = Contact.objects.order_by('name') 

   return render(
      request, 
      'contact.html', 
      {
         'title':'Contacts', 
         'message':'Your contact page looks like this bana.',
         'year':datetime.datetime.now().year, 
         'contact_list': contact_list, # Embed data into the HttpResponse object
      }
   )