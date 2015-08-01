from django.db import models
from django.template.defaultfilters import default

# Create your models here.

class FirstModel(models.Model):
    Username = models.CharField(max_length=20)


class SecondModel(models.Model):
    Nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20,default='hanxin')
    Address = models.CharField(max_length=10,default='alex')
    Gender = models.NullBooleanField()
    Age = models.IntegerField(default=1)
    Date = models.DateField()

class ThirdModel(models.Model):
    Price = models.DecimalField(max_digits=10,decimal_places=2)
    