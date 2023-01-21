from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=90)
    email = models.EmailField(max_length=254)
    mobile = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name
    
class Signup(models.Model):
    email1 = models.EmailField(max_length=254)
    email2 = models.EmailField(max_length=254)
    password1 = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    mobile = models.CharField(max_length=15)

    def __str__(self):
        return self.fname
    

class Signup1(models.Model):
    email1 = models.EmailField(max_length=254)
    email2 = models.EmailField(max_length=254)
    password1 = models.CharField(max_length=200)
    password2 = models.CharField(max_length=200)
    cname = models.CharField(max_length=500)
    cindustry = models.CharField(max_length=500)
    location = models.CharField(max_length=300)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=200)
    cpname = models.CharField(max_length=500)
    cpmobile = models.CharField(max_length=20)
    cpemail = models.EmailField(max_length=254)

    def __str__(self):
        return self.cpname

class Popular(models.Model):
    logo1 = models.ImageField(upload_to='images', default="")
    title1 = models.CharField(max_length=500, default="")
    company1 = models.CharField(max_length=500, default="")
    address1 = models.CharField(max_length=200, default="")
    cinfo1 = models.TextField(default="")
    jinfo1 = models.TextField(default="")

    logo2 = models.ImageField(upload_to='images', default="")
    title2 = models.CharField(max_length=500, default="")
    company2 = models.CharField(max_length=500, default="")
    address2 = models.CharField(max_length=200, default="")
    cinfo2 = models.TextField(default="")
    jinfo2 = models.TextField(default="")

    logo3 = models.ImageField(upload_to='images', default="")
    title3 = models.CharField(max_length=500, default="")
    company3 = models.CharField(max_length=500, default="")
    address3 = models.CharField(max_length=200, default="")
    cinfo3 = models.TextField(default="")
    jinfo3 = models.TextField(default="")

    logo4 = models.ImageField(upload_to='images', default="")
    title4 = models.CharField(max_length=500, default="")
    company4 = models.CharField(max_length=500, default="")
    address4 = models.CharField(max_length=200, default="")
    cinfo4 = models.TextField(default="")
    jinfo4 = models.TextField(default="")

    def __str__(self):
        return self.company1

   
    

    
