from import_export import resources
from .models import Vehiculo

class VehiculoResource(resources.ModelResource):
    class Meta:
        model = Vehiculo
