from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    nombre = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    