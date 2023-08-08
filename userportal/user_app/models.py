from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=50,unique=True)
    email = models.CharField(max_length=200,unique=True,null=False)
    password = models.CharField(max_length=200,null=False)
    mobile = models.CharField(max_length=10,unique=True,null=False)


    def __str__(self):
        return f"{self.email}"