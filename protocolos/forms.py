from django import forms
from .models import VersionDocumento, Documento

class CrearDocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ['clase','nombre', 'codigo']

class VersionDocumentoForm(forms.ModelForm):
    class Meta:
        model = VersionDocumento
        fields = ['archivo_pdf', 'archivo_word', 'fecha_creacion', 'fecha_revision', 'fecha_implementacion']
        widgets = {
            'archivo_pdf': forms.FileInput(attrs={'accept': '.pdf'}),
            'archivo_word': forms.FileInput(attrs={'accept': '.doc, .docx, .txt'}),
            'fecha_creacion': forms.DateTimeInput(attrs={'type': 'date'}),
            'fecha_revision': forms.DateTimeInput(attrs={'type': 'date'}),
            'fecha_implementacion': forms.DateTimeInput(attrs={'type': 'date'}),
        }
