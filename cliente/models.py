from django.db import models

# Create your models here.
# model customer
class Customer(models.Model):
    name=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    cityOfResidence=models.CharField(max_length=50)
    birthDate=models.DateField()
    