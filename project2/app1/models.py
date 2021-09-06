from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import redirect


class Employee(models.Model):
    ename = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    esalary = models.FloatField()
    edate = models.DateField(auto_now=True)
    status = models.BooleanField(default=1)
    createdby=models.ForeignKey(User,on_delete=models.CASCADE,default=1)

# Create your models here.


class Student(models.Model):
    sname = models.CharField(max_length=25)
    branch = models.CharField(max_length=20)
    roll_no = models.CharField(max_length=15)
    college = models.CharField(max_length=30)
    fees = models.IntegerField()
    status =models.BooleanField(default=1)

class Customer(models.Model):
    cname = models.CharField(max_length=25)
    email = models.CharField(max_length=20)
    phone = models.BigIntegerField()
    village = models.CharField(max_length=30)
    order = models.CharField(max_length=20)
    status =models.BooleanField(default=1)

    '''def get_absolute_url(self):
        return redirect('/list')'''

class Books(models.Model):
    date= models.DateField()
    sub = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.BigIntegerField()
    price = models.FloatField()
    status = models.BooleanField(default=True)


class Movies(models.Model):
    mtitle = models.CharField(max_length=30)
    hero =models.CharField(max_length=30)
    heroin =models.CharField(max_length=30)
    desc = models.CharField(max_length=100)
    release_date=models.DateField()
    status = models.BooleanField(default=True)
    mimage = models.ImageField(upload_to='movies',default='alt.png')





