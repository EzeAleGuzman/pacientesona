from django.db import models
import os
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver




    
class Documento(models.Model):
    OPCIONES_CLASE = [
        ('Normativa General', 'Normativa General') ,
        ('Protocolos de Control de Infecciones', 'Protocolos de Control de Infecciones'),
        ('Protocolos Generales','Protocolos Generales'),
        ('Protocolos de Servicios', 'Protocolos de Servicios'),
        ('Instructivo de procedimientos', 'Instructivo de procedimientos'),
        
    ]
    clase = models.CharField(max_length=50, choices=OPCIONES_CLASE,blank=True,null=True)
    nombre = models.CharField(max_length=100, unique=True)
    codigo = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class VersionDocumento(models.Model):
    documento = models.ForeignKey(Documento, on_delete=models.CASCADE, related_name='versiones')
    version = models.PositiveIntegerField()
    archivo_pdf = models.FileField(upload_to='pdf/')
    archivo_word = models.FileField(upload_to='word/')
    fecha_creacion = models.DateTimeField(null=True, blank=True)
    fecha_subida = models.DateTimeField(auto_now_add=True, editable=False)
    fecha_revision = models.DateTimeField(null=True, blank=True)
    fecha_implementacion = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.documento}-version: {self.version}'

def eliminar_archivo(sender, instance, **kwargs):
    if instance.archivo_pdf:
        if os.path.isfile(instance.archivo_pdf.path):
            os.remove(instance.archivo_pdf.path)
    elif instance.archivo_word:
        if os.path.isfile(instance.archivo_word.path):
            os.remove(instance.archivo_word.path)

@receiver(pre_delete, sender=VersionDocumento)
def eliminar_archivo_en_pre_delete(sender, instance, **kwargs):
    eliminar_archivo(sender, instance)

@receiver(pre_save, sender=VersionDocumento)
def actualizar_version(sender, instance, **kwargs):
    if instance.pk is None:
        ultima_version = VersionDocumento.objects.filter(documento=instance.documento).order_by('-version').first()
        instance.version = 1 if ultima_version is None else ultima_version.version + 1