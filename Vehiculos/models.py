from django.db import models

class Vehiculo(models.Model):
    
    patente = models.CharField(max_length=80, blank=True)
    modelo = models.CharField(max_length=80, blank=True)
    agente = models.CharField(max_length=80, blank=True)
    servicio = models.CharField(max_length=50, blank=True)
    telefono = models.CharField(max_length=80, blank=True)

    
    def __str__(self):
        return f"{self.patente} {self.agente}"