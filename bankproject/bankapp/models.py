


from django.db import models


# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=250)
    name=models.CharField(max_length=250)
    password=models.CharField(max_length=250)
    email=models.CharField(max_length=250)
    gender=models.CharField(max_length=250)
    country=models.CharField(max_length=250)
   
class Personal(models.Model):
    Firstname=models.CharField(max_length=250)
    Lastname=models.CharField(max_length=250)
    Email=models.CharField(max_length=250)
    Phone_number=models.CharField(max_length=250)
    dob=models.DateField
    Gender=models.CharField(max_length=250)
    age=models.DecimalField
    Address=models.CharField(max_length=250)
    district=models.CharField(max_length=250)
    account_type=models.CharField(max_length=250)
    material = models.BooleanField(default=False)
    