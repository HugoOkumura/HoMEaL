from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class CustomUser(AbstractBaseUser):
    is_manager = models.BooleanField(default=False)
    nome = models.CharField(max_length=50)
    senha = models.CharField(max_length=50)
    endereco = models.CharField(max_length=150)

