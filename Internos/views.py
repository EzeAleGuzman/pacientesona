from django.shortcuts import render, get_object_or_404
from .models import Interno

def ver_interno(request):
    internos = Interno.objects.all()
    return render(request, 'internos.html', {'internos' : internos})

def buscar_interno(request):
    query = request.GET.get('q', '')
    internos = Interno.objects.filter(patente__icontains=query)
    return render(request, 'buscar_interno.html', {'internos': internos, 'query': query})


