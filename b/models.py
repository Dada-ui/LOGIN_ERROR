from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Home_Model(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Login_Model(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)