from django import forms
from .models import  Solicitud

class FormularioSolicitud(forms.ModelForm):


    class Meta:

        model =Solicitud
        fields  = ['usuario', 'sala','descripcion', 'horario']


class FormularioRepuesta(forms.ModelForm):

    
    class Meta:
        
        model= Solicitud
        fields = ['usuario', 'sala','descripcion', 'horario','respuesta']