from django.db import models

# Create your models here.
class Data(models.Model):
    rollno=models.IntegerField()
    name=models.CharField(max_length=100)
    middle=models.CharField(max_length=100)
    surname=models.CharField(max_length=100)
    mobileno=models.IntegerField()
    email=models.EmailField(max_length=80)
    address=models.CharField(max_length=200)
    password=models.CharField(max_length=100)

