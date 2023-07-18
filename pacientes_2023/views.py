from django.shortcuts import render,get_object_or_404, redirect
from .forms import PacienteForm
from .models import Paciente
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages




def pacientes_por_servicio(request, servicio):
    pacientes = Paciente.objects.filter(servicio=servicio)
    context = {
        'pacientes': pacientes,
        'servicio': servicio,
    }
    return render(request, 'pacientes_por_servicio.html', context)


def salir(request):
    logout(request)
    return redirect('/')

@login_required
def agregar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        form.save()
        messages.success(request, 'Paciente Agregado exitosamente.')
        return redirect('index')
        
    else:
        form = PacienteForm()
        
    return render(request, 'agregar_paciente.html', {'form': form})

@login_required
def index(request):
    pacientes = Paciente.objects.all()
    servicios = Paciente.objects.values_list('servicio', flat=True).distinct()
    return render(request, 'index.html', {'pacientes': pacientes, 'servicios': servicios})

@login_required
def borrar_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    paciente.delete()
    messages.success(request, 'Paciente Eliminado exitosamente.')
    return redirect('index')


@login_required
def editar_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)

    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Paciente Editado exitosamente.')
            return redirect('index')
    else:
        form = PacienteForm(instance=paciente)

    return render(request, 'editar_paciente.html', {'form': form})
