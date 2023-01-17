from django.shortcuts import render, HttpResponse
from . models import *
# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services1(request):
    return render(request, 'services1.html')

def services2(request):
    return render(request, 'services2.html')

def services3(request):
    return render(request, 'services3.html')

def help(request):
    return render(request, 'help.html')

def contact(request):
    return render(request, 'contact.html')
