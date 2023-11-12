from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Paciente

class PacienteAdmin(ImportExportModelAdmin):
    list_display = ['nombre', 'apellido', 'servicio', 'habitacion', 'cama', 'diagnostico']
    list_filter = ['servicio']
    search_fields = ['nombre', 'apellido', 'habitacion', 'cama']

    def has_view_permission(self, request, obj=None):
        return request.user.has_perm('paciente_2023.view_paciente')

    def has_add_permission(self, request):
        return request.user.has_perm('paciente_2023.add_paciente')

    def has_change_permission(self, request, obj=None):
        return request.user.has_perm('paciente_2023.change_paciente')

    def has_delete_permission(self, request, obj=None):
        return request.user.has_perm('paciente_2023.delete_paciente')

admin.site.register(Paciente, PacienteAdmin)
