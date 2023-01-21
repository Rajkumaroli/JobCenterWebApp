from django.shortcuts import render, HttpResponse
from . models import *
from django.contrib import messages
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
    if request.method=='POST':
        name = request.POST["name"]
        email = request.POST["email"]
        mobile = request.POST["mobile"]
        message = request.POST["message"]
        if len(name)<2 or len(email)<3 or len(mobile)<10:
            messages.error(request, "All field is Required!!")
        else:
            data = Contact.objects.create(name=name,email=email,mobile=mobile,message=message)
            data.save()
            messages.success(request, "Thanks for contacting us! We will be in touch with you shortly.")
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    if request.method=='POST':
        email1= request.POST["email1"]
        email2= request.POST["email2"]
        password1= request.POST["password1"]
        password2 = request.POST["password2"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        mobile = request.POST["mobile"]
        if len(fname)<2 or len(email1)<3 or len(mobile)<10:
            messages.error(request, "All field is Required!!")
        else:
            data = Signup.objects.create(email1=email1, email2=email2,password1=password1,password2=password2,fname=fname,lname=lname,mobile=mobile)
            data.save()
            messages.success(request, "Your account create Successfully...")
    return render(request, 'signup.html')

def signup1(request):
    if request.method=='POST':
        email1= request.POST["email1"]
        email2= request.POST["email2"]
        password1= request.POST["password1"]
        password2 = request.POST["password2"]
        cname = request.POST["cname"]
        cindustry = request.POST["cindustry"]
        location = request.POST["location"]
        phone = request.POST["phone"]
        city = request.POST["city"]
        cpname = request.POST["cpname"]
        cpmobile = request.POST["cpmobile"]
        cpemail = request.POST["cpemail"]
        if len(cname)<2 or len(email1)<3 or len(cpmobile)<10:
            messages.error(request, "All field is Required!!")
        else:
            data = Signup1.objects.create(email1=email1, email2=email2,password1=password1,password2=password2,cname=cname, cindustry=cindustry, location=location, phone=phone, city=city,cpname=cpname, cpmobile=cpmobile, cpemail=cpemail)
            data.save()
            messages.success(request, "Your account create Successfully...")
    return render(request, 'signup1.html')

def popular(request):
    jobs = Popular.objects.all()
    return render(request, 'popular.html', {'jobs':jobs})

def fulltime(request):
    return render(request, 'fulltime.html')

def parttime(request):
    return render(request, 'parttime.html')