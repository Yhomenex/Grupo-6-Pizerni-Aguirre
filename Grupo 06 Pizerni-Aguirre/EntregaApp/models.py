from django.db import models

# Create your models here.
class Videojuego(models.Model):
    nombre=models.CharField(max_length=40)
    categoria=models.CharField(max_length=40)

class Torneo(models.Model):
    nombre=models.CharField(max_length=40)
    pais=models.CharField(max_length=40)
    premio=models.IntegerField()
    descripcion=models.CharField(max_length=240)
    

class Equipo(models.Model):
    nombre=models.CharField(max_length=40)
    nacionalidad=models.CharField(max_length=40)
    cantidad_integrantes=models.IntegerField()

    def __str__(self):
        return f"NOMBRE: {self.nombre} - NACIONALIDAD: {self.nacionalidad} - CANTIDAD_INTEGRANTES: {self.cantidad_integrantes}"