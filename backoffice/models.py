from datetime import datetime

from django.db import models

# Create your models here.


class Animal(models.Model):
    nombre = models.CharField(max_length=30)


class Raza(models.Model):
    nombre = models.CharField(max_length=30)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, null=True, blank=True)


class Diagnostico(models.Model):
    nombre = models.CharField(max_length=50)
    comentarios = models.CharField(max_length=500, null=True, blank=True)
    tratamiento= models.CharField(max_length=200, null=True, blank=True)
    precio = models.DecimalField(default=0, max_digits=6, decimal_places=2, null=True, blank=True)


class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    peso = models.DecimalField(default=0, max_digits=6, decimal_places=2, null=True, blank=True)
    edad = models.CharField(max_length=50, null=True, blank=True)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, null=True, blank=True)
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE, null=True, blank=True)
    dueno = models.CharField(max_length=50, null=True, blank=True)
    celular = models.CharField(max_length=15, null=True, blank=True)
    correo = models.CharField(max_length=50, null=True, blank=True)


class Historial(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    diagnostico = models.ForeignKey(Diagnostico, on_delete=models.CASCADE, null=True, blank=True)
    fecha = models.DateTimeField(default=datetime.now, null=True, blank=True)
    comentario = models.CharField(max_length=500, null=True, blank=True)


