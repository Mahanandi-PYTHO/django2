from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class companies(models.Model):
    cname=models.CharField(max_length=50)
    skills=models.CharField(max_length=300)
    roles=models.CharField(max_length=30)
    address=models.CharField(max_length=80)
    logo=models.ImageField(upload_to='media',default='alt.jpg')



