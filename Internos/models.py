from django.db import models


class Interno(models.Model):
    servicio = models.CharField(max_length=80, blank=False)
    interno = models.CharField(max_length=80, blank=True)
    
    
    
    def __str__(self):
        return f"{self.interno} {self.servicio}"