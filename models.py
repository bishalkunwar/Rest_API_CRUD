from django.db import models

# Create your models here.

class student(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    email = models.EmailField(max_length=100)
