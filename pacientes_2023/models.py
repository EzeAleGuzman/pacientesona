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
    servicio = models.CharField(max_length=50, choices=OPCIONES_SERVICIO,blank=True, null=True)
    habitacion = models.CharField(max_length=80,)
    cama = models.CharField(max_length=80,blank=True,null=True)
    diagnostico = models.TextField(max_length=80, default='Sin diagnóstico')
    fecha_ingreso = models.DateField(null=True, blank=True)
    fecha_egreso = models.DateField(null=True, blank=True)
    OPCIONES_ESTADO = [
        ('Internado', 'Continúa internado'),
        ('Dado de alta', 'Dado de alta'),
        ('Se fue sin alta médica', 'Se fue sin alta médica'),
        ('Derivado', 'Fue derivado'),
        ('Óbito', 'Óbito'),
    ]
    estado = models.CharField(max_length=50, choices=OPCIONES_ESTADO, default='Internado')

    anotaciones = models.TextField(blank=True, null=True)


class Meta:
        permissions = [
            ("view_paciente", "Can view Paciente"),
            ("add_paciente", "Can add Paciente"),
            ("change_paciente", "Can change Paciente"),
            ("delete_paciente", "Can delete Paciente"),
        ]

        def __str__(self):
            return f"{self.nombre} {self.apellido} {self.servicio} {self.habitacion} {self.cama} {self.diagnostico} "