from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=90)
    email = models.EmailField(max_length=254)
    mobile = models.CharField(max_length=20)
    message = models.TextField()