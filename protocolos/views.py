from django.shortcuts import render, redirect
from .forms import CrearDocumentoForm, VersionDocumentoForm
from django.contrib import messages
from .models import Documento
from django.http import JsonResponse



def cargar_documento(request):
    messages.error = None
    if request.method == 'POST':
        crear_documento_form = CrearDocumentoForm(request.POST)
        if crear_documento_form.is_valid():
            clase_documento = crear_documento_form.cleaned_data['clase']
            nombre_documento = crear_documento_form.cleaned_data['nombre']
            codigo_documento = crear_documento_form.cleaned_data['codigo']

            documento, creado = Documento.objects.get_or_create(clase=clase_documento, nombre=nombre_documento, codigo=codigo_documento)

            if creado:
                messages.success(request, "¡El documento se ha creado correctamente!")
                return redirect('agregar_version', documento_id=documento.id)
            else:
                messages.error(request, "¡El documento ya existe!")
                return redirect('cargar_documento')
    else:
        crear_documento_form = CrearDocumentoForm()
        
    documentos = Documento.objects.all()
    context = {'crear_documento_form': crear_documento_form, 'documentos': documentos}
    return render(request, 'protocolos.html', context)

def documentos_por_clase(request, clase):
    documentos = Documento.objects.filter(clase=clase)
    context = {
        'documentos': documentos,
        'clase': clase,
    }
    return render(request, 'protocolos.html', context)

def listarData(request):
    documentos = Documento.objects.all()
    return render(request=request, template_name="list_img_file.html", context={'documentos': documentos})

def agregar_version(request, documento_id):
    try:
        documento = Documento.objects.get(id=documento_id)
    except Documento.DoesNotExist:
        return redirect('cargar_documento')  # Redirigir si el documento no existe
    
    if request.method == 'POST':
        version_documento_form = VersionDocumentoForm(request.POST, request.FILES)
        if version_documento_form.is_valid():
            version_documento = version_documento_form.save(commit=False)
            version_documento.documento = documento
            version_documento.save()
            return redirect('cargar_documento') 
    else:
        version_documento_form = VersionDocumentoForm()
        
    return render(request, 'versionprotocolo.html', {'documento': documento, 'version_documento_form': version_documento_form})
