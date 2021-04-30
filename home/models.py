from django.db import models
from django.conf import settings
from django.db.models.enums import Choices

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50,default="")
    email = models.EmailField()
    subject = models.CharField(max_length=50,default="")
    message = models.CharField(max_length=250,default="")


    def __str__(self) :
        return self.name


class Image(models.Model):
    
    place=models.CharField(max_length=100)
    description=models.CharField(max_length=100000,default="")
    days=models.IntegerField(default="")
    image=models.ImageField(upload_to="img/%y")
    money=models.IntegerField(default="0")

    def __str__(self):
        return self.place


class Hotels(models.Model):
    myyid = models.AutoField
    hotel_name=models.CharField(max_length=100)
    desc=models.CharField(max_length=100000,default="")
    hotel_img=models.ImageField(upload_to="img/%y")
    price=models.IntegerField(default="0")

    def __str__(self):
        return self.hotel_name


class Booking(models.Model):
    bookid = models.AutoField
    travellers = models.IntegerField(default="")
    hotel_name = models.CharField(max_length=100,default="")





