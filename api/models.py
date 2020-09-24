from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Moneysend(models.Model):
    sender =models.CharField(max_length=255)
    receiver =models.CharField(max_length=254)
    amount = models.CharField(max_length=255, default=0)
    description = models.CharField(max_length=255,default="Payment Processed on")
    paymenton =models.DateTimeField(auto_now=True)


class Profile(models.Model):
   
    telephone = models.CharField(max_length=255)
   
    verification= models.CharField(max_length=255)
    status = models.CharField(max_length=255)
   
    def __str__(self):
        return self.telephone

class Paybills(models.Model):
    sender =models.CharField(max_length=255)
    receiver =models.CharField(max_length=254)
    amount = models.CharField(max_length=255, default=0)
    description = models.CharField(max_length=255,default="Payment Processed on")
    paymenton =models.DateTimeField(auto_now=True)