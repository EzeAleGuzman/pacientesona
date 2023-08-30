from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Vehiculo
from .resources import VehiculoResource

@admin.register(Vehiculo)
class VehiculoAdmin(ImportExportModelAdmin):
    resource_class = VehiculoResource
    
    # Para omitir filas vacías y omitir filas sin cambios en la importación
    def import_data(self, dataset, dry_run=False, *args, **kwargs):
        kwargs['skip_unchanged'] = True
        kwargs['skip_rows_with_empty_values'] = True  # Omitir filas vacías
        return super().import_data(dataset, dry_run, *args, **kwargs)
