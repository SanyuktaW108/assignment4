from django.db import models
# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    address=models.CharField(max_length=50)

