from django.contrib import admin
from .models import Documento, VersionDocumento

class VersionDocumentoInline(admin.TabularInline):
    model = VersionDocumento
    extra = 0

class DocumentoAdmin(admin.ModelAdmin):
    inlines = [VersionDocumentoInline]

admin.site.register(Documento, DocumentoAdmin)
admin.site.register(VersionDocumento)

