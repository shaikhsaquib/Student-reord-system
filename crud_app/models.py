from django.db import models
# import django.utils.datetime_safe
# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField( max_length=254)
    password=models.CharField(max_length=50)
    standard=models.CharField(null=False, max_length=50)
    def __str__(self):
        return self.name
    


