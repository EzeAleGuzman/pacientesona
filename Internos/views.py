from django.shortcuts import render, get_object_or_404, redirect,HttpResponse
from .forms import InternoForm, EditarInternoForm
from .models import Interno
from django.contrib import messages

def ver_interno(request):
    internos = Interno.objects.all().order_by('servicio')
    form = InternoForm()
    edit_form = EditarInternoForm
    
    context = {
        'internos': internos,
        'form' : form,
        'edit_form' : edit_form
        }   
    return render(request, 'internos.html',context)


def agregar_interno(request):
    
    if request.POST:
        form = InternoForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
            except: 
                messages(request, 'Error al guardar el interno')
                return redirect('internos')
    

    return redirect('internos')


def buscar_interno(request):
    query = request.GET.get('q', '')
    internos = Interno.objects.filter(patente__icontains=query)
    return render(request, 'buscar_interno.html', {'internos': internos, 'query': query})



def borrar_interno(request, interno_id):
    interno = get_object_or_404(Interno, id=interno_id)
    if request.method == 'POST':
        interno.delete()
        messages.success(request, 'Interno Eliminado')
    return redirect('internos')

def editar_interno(request, interno_id):
    interno = get_object_or_404(Interno, pk=interno_id)
    
    if request.method == 'POST':
        form = EditarInternoForm(request.POST, request.FILES, instance=interno)
        if form.is_valid():
            form.save()
            return redirect('internos')  # Reemplaza con el nombre de tu vista de lista
    else:
        form = EditarInternoForm(instance=interno)

    return render(request, 'editar_internos.html', {'form': form})
