from django.forms import ModelForm, DateInput
from .models import Paciente
from django import forms

class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido', 'servicio', 'habitacion', 'cama', 'diagnostico', 'fecha_ingreso', 'fecha_egreso', 'estado', 'anotaciones']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'bg-zinc-300 p-3 rounded-lg block w-full mb-3 hover:shadow-md hover:shadow-zinc-500/50 border border-black'}),
            'apellido': forms.TextInput(attrs={'class': 'bg-zinc-300 p-3 rounded-lg block w-full mb-3 hover:shadow-md hover:shadow-zinc-500/50 border border-black'}),
            'servicio': forms.Select(attrs={'class': 'bg-zinc-300 p-3 rounded-lg block w-full mb-3 hover:shadow-md hover:shadow-zinc-500/50 border border-black'}),
            'habitacion': forms.TextInput(attrs={'class': 'bg-zinc-300 p-3 rounded-lg block w-full mb-3 hover:shadow-md hover:shadow-zinc-500/50 border border-black'}),
            'cama': forms.TextInput(attrs={'class': 'bg-zinc-300 p-3 rounded-lg block w-full mb-3 hover:shadow-md hover:shadow-zinc-500/50 border border-black'}),
            'diagnostico': forms.TextInput(attrs={'class': 'bg-zinc-300 p-3 rounded-lg block w-full mb-3 hover:shadow-md hover:shadow-zinc-500/50 border border-black'}),
            'fecha_ingreso': DateInput(attrs={'type': 'date', 'class': 'bg-zinc-300 p-3 rounded-lg block w-full mb-3 hover:shadow-md hover:shadow-zinc-500/50 border border-black'}),
            'fecha_egreso': DateInput(attrs={'type': 'date', 'class': 'bg-zinc-300 p-3 rounded-lg block w-full mb-3 hover:shadow-md hover:shadow-zinc-500/50 border border-black'}),
            'estado': forms.Select(attrs={'class': 'bg-zinc-300 p-3 rounded-lg block w-full mb-3 hover:shadow-md hover:shadow-zinc-500/50 border border-black'}),
            'anotaciones': forms.Textarea(attrs={'class': 'bg-zinc-300 p-3 rounded-lg block w-full mb-3 hover:shadow-md hover:shadow-zinc-500/50 border border-black'}),
        }
