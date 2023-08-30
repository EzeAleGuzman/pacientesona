from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Paciente

class PacienteAdmin(ImportExportModelAdmin):
    list_display = ['nombre', 'apellido', 'servicio', 'habitacion', 'cama', 'diagnostico']
    list_filter = ['servicio']
    search_fields = ['nombre', 'apellido', 'habitacion', 'cama']
    
admin.site.register(Paciente, PacienteAdmin)
