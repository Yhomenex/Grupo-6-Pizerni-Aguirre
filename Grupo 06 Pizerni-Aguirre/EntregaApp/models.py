from itertools import pairwise
from django.db import models

# Create your models here.
class Videojuego(models.Model):
    nombre=models.CharField(max_length=40)
    categoria=models.CharField(max_length=40)

class Torneo(models.Model):
    nombre=models.CharField(max_length=40)
    pais=models.CharField(max_length=40)
    premio=models.IntegerField()
    descripcion=models.CharField(max_length=40, null=True)
    

class Equipo(models.Model):
    nombre=models.CharField(max_length=40)
    nacionalidad=models.CharField(max_length=40)
    cantidad_integrantes=models.IntegerField()
