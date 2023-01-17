from django.urls import path
from mainapp.views import *

urlpatterns = [
    path('',home, name='home'),
    path('about/',about, name='about'),
    path('services1/',services1, name='services1'),
    path('services2/', services2, name='services2'),
    path('services3/', services3, name='services3'),
    path('help/', help, name='help'),
    path('contact/', contact, name='contact')
]
