from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserType(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    type = models.CharField(max_length=50)

class user_reg(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    mobile =models.CharField(max_length=100,null=True)
    con_password =models.CharField(max_length=100,null=True)
    
class driver_reg(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    mobile=models.CharField(max_length=100,null=True)
    license_no=models.ImageField(null=True)
    experience=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=100,null=True)
    pincode=models.CharField(max_length=100,null=True)
    con_password =models.CharField(max_length=100,null=True)
    image=models.ImageField(null=True)
    status=models.CharField(max_length=100,null=True)
    veh_type=models.CharField(max_length=100,null=True)

class staff_reg(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    mobile=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=100,null=True)
    pincode=models.CharField(max_length=100,null=True)
    con_password =models.CharField(max_length=100,null=True)

class location(models.Model):
    location= models.CharField(max_length=50, null=True)


class trips(models.Model):
    user = models.ForeignKey(user_reg,on_delete=models.CASCADE,null=True)
    driver=models.ForeignKey(driver_reg,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=100,null=True)
    pickup_place=models.CharField(max_length=100,null=True)
    to_place=models.CharField(max_length=100,null=True)
    mobile=models.CharField(max_length=100,null=True)
    time=models.CharField(max_length=100,null=True)
    date=models.DateField(max_length=100,null=True)
    car_type=models.CharField(max_length=100,null=True)
    status=models.CharField(max_length=100,null=True)
    km_per_amt=models.IntegerField(max_length=100,null=True)
    kms=models.IntegerField(max_length=100,null=True)
    total_amt=models.CharField(max_length=100,null=True)
    payment=models.CharField(max_length=100,null=True)
   

