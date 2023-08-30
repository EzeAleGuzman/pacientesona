from django.db import models

# Create your models here.
class Paciente(models.Model):

    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    OPCIONES_SERVICIO = [
    ('Clinica Medica', 'Clinica Medica'),
        ('Guardia Adultos', 'Guardia de Adultos'),
        ('Maternidad', 'Maternidad'),
        ('Neo', 'Neo'),
        ('Partos', 'Partos'),
        ('Pediatria Guardia', 'Pedriatria Guardia'),
        ('Pediatria Internacion', 'Pediatria Internacion'),
        ('Polivalente', 'Polivalente'),
        ('Quirofano', 'Quirofano'),
        ('UCI', 'UCI'),
        ('UTI', 'UTI'),
        ('Coordinacion', 'Coordinacion'),
        ('Casa de Madres', 'Casa de Madres'),
    ]
    servicio = models.CharField(max_length=50, choices=OPCIONES_SERVICIO)
    habitacion = models.CharField(max_length=80)
    cama = models.CharField(max_length=80)
    diagnostico = models.TextField(max_length=80)


    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.servicio} {self.habitacion} {self.cama} "