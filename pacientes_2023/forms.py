from django.forms import  ModelForm
from .models import Paciente
from django import forms

class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido','servicio', 'habitacion', 'cama' ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'bg-zinc-300 p-3 rounded-lg block w-full mb-3 hover:shadow-md hover:shadow-zinc-500/50'}),
            'apellido': forms.TextInput(attrs={'class': 'bg-zinc-300 p-3 rounded-lg block w-full mb-3 hover:shadow-md hover:shadow-zinc-500/50'}),
            'servicio': forms.Select(attrs={'class': 'class="flex justify-end absolute top-4 right-4 z-10 bg-white border rounded px-3 py-2"'}),
            'habitacion': forms.TextInput(attrs={'class': 'bg-zinc-300 p-3 rounded-lg block w-full mb-3 hover:shadow-md hover:shadow-zinc-500/50'}),
            'cama': forms.TextInput(attrs={'class': 'bg-zinc-300 p-3 rounded-lg block w-full mb-3 hover:shadow-md hover:shadow-zinc-500/50'}),
            
        }