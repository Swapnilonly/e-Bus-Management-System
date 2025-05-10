from django.db import models

# Create your models here.
class Usersignup(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phnum = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    password = models.CharField(max_length=12)

class PostBusInfo(models.Model):
    busnumber = models.CharField(max_length=15)
    routename = models.CharField(max_length=40)
    departuretime = models.CharField(max_length=10)
    arrivaltime = models.CharField(max_length=10)
    busfair = models.CharField(max_length=5)

class PostBusContact(models.Model):
    contactperson = models.CharField(max_length=30)
    contactemail = models.EmailField(max_length=40)
    contactphone = models.CharField(max_length=10)
    contactaddress = models.CharField(max_length=30)

class PostBusType(models.Model):
    bustype = models.CharField(max_length=10)
    buscapacity = models.CharField(max_length=10)
    buscdescription = models.CharField(max_length=50)

class Busbooking(models.Model):
    busnumber = models.CharField(max_length=10)
    travel_date = models.DateField(max_length=10)
    numseats = models.CharField(max_length=10)

