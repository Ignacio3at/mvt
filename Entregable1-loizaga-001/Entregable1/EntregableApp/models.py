from django.db import models
from django.forms import CharField, IntegerField


# Create your models here.

class Familiares(models.Model):
    nombre = models.CharField(max_length=40, default = None)
    apellido = models.CharField(max_length=40, default = None)
    fechaDeNacimiento = models.DateField(default = None)
    edad = models.IntegerField(default = None)


