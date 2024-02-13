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
        messages.success(request, 'Paciente Agregado')
        return redirect('index')

    else:
        form = PacienteForm()

    return render(request, 'agregar_paciente.html', {'form': form})

@login_required
def pacientes_no_internados(request):
    pacientes = Paciente.objects.exclude(estado='Internado').order_by('habitacion')
    estados = Paciente.objects.values_list('estado').distinct()
    pertenece_admin = request.user.groups.filter(name='admins').exists()
    pertenece_Cuidadores = request.user.groups.filter(name='Cuidadores').exists()

    return render(request, 'pacientes_no_internados.html', {
        'pacientes': pacientes,
        'estados': estados,
        'pertenece_admin': pertenece_admin,
        'pertenece_Cuidadores': pertenece_Cuidadores
    })


@login_required
def index(request):
    pacientes = Paciente.objects.all()
    servicios = Paciente.objects.values_list('servicio', flat=True).distinct()
    pacientes = Paciente.objects.filter(estado='Internado').order_by('habitacion')
    pertenece_admin = request.user.groups.filter(name='admins').exists()
    pertenece_Cuidadores = request.user.groups.filter(name='Cuidadores').exists()
    return render(request, 'index.html', {'pacientes': pacientes, 'servicios': servicios,'pertenece_admin': pertenece_admin, 'pertenece_Cuidadores' : pertenece_Cuidadores})

@login_required
def borrar_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    if request.method == 'POST':
        paciente.delete()
        messages.success(request, 'Paciente Eliminado')
    return redirect('index')


@login_required
def editar_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)

    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Paciente Editado')
            return redirect('index')
    else:
        form = PacienteForm(instance=paciente)

    return render(request, 'editar_paciente.html', {'form': form})
