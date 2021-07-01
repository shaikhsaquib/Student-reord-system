from django.db import models
import django.utils.datetime_safe
# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField( max_length=254)
    password=models.CharField(max_length=50)


