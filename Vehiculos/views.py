from django.shortcuts import render, get_object_or_404
from .models import Vehiculo

def ver_vehiculos(request):
    cantidad_vehiculos = 10
    vehiculos = Vehiculo.objects.all()[:cantidad_vehiculos]
    return render(request, 'vehiculos.html', {'vehiculos' : vehiculos})

def buscar_vehiculo(request):
    query = request.GET.get('q', '')
    vehiculos = Vehiculo.objects.filter(patente__icontains=query)
    return render(request, 'buscar_vehiculo.html', {'vehiculos': vehiculos, 'query': query})

def ver_ficha_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, pk=vehiculo_id)
    return render(request, 'ver_ficha_vehiculo.html', {'vehiculo': vehiculo})
