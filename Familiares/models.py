from django.db import models

class Novia(models.Model):
    nombre = models.CharField(max_length=40)
    documento=models.CharField(max_length=40)
    fecha_nacimiento=models.DateField()

class Madre(models.Model):
    nombre1 = models.CharField(max_length=40)
    documento1=models.CharField(max_length=40)
    fecha_nacimiento1=models.DateField()

class Hermano(models.Model):
    nombre2 = models.CharField(max_length=40)
    documento2=models.CharField(max_length=40)
    fecha_nacimiento2=models.DateField()