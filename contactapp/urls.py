from django import views
from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='homepage'),
    path('contact/', contact, name='contatc'),
]