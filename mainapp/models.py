from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserData(models.Model):
    gen = [
        ("Masculino", "Masculino"),
        ("Femenino", "Femenino")
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="userdata")
    especialiad = models.CharField(max_length=50, null=True)
    sexo = models.CharField(max_length=50, choices=gen)
    telefono = models.CharField(max_length=50, null=True)
    centro = models.CharField(max_length=50, null=True)

