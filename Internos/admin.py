from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Interno

class InternoAdmin(ImportExportModelAdmin):
    list_display = ['servicio', 'interno']
    list_filter = ['servicio']
    search_fields = ['servicio', 'interno']

    
admin.site.register(Interno, InternoAdmin)
