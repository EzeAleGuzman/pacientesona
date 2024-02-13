from django import forms
from .models import Interno


class InternoForm(forms.ModelForm):
    
    class Meta:
        model = Interno
        fields = '__all__'


class EditarInternoForm(forms.ModelForm):
    
    class Meta: 
        model = Interno
        fields = '__all__'
        widgets = {
           'servicio':forms.TextInput(attrs={'type': 'text', 'id' : 'servicio_editar'}),
           'interno':forms.TextInput(attrs={'id' : 'interno_editar'}),
        }
        
        